import os

try:
    from google import genai
except ImportError:  # pragma: no cover
    genai = None


class GeminiServiceError(RuntimeError):
    """Raised when Gemini cannot be called."""


def generate_with_gemini(prompt: str) -> str:
    """Send a prompt to Gemini and return text output.

    This function expects GEMINI_API_KEY to be available in your environment.
    For local development, create a .env file based on .env.example.
    """
    if genai is None:
        raise GeminiServiceError(
            "google-genai is not installed. Install project dependencies first."
        )

    api_key = os.getenv("GEMINI_API_KEY")
    if not api_key:
        raise GeminiServiceError(
            "Missing GEMINI_API_KEY. Add it to your environment or local .env file."
        )

    model_name = os.getenv("GEMINI_MODEL", "gemini-1.5-flash")

    try:
        client = genai.Client(api_key=api_key)
        response = client.models.generate_content(
            model=model_name,
            contents=prompt,
        )
    except Exception as exc:
        raise GeminiServiceError(
            f"Gemini request failed using model '{model_name}': {exc}"
        ) from exc

    text = getattr(response, "text", None)
    if not text:
        raise GeminiServiceError("Gemini returned an empty response.")

    return text
