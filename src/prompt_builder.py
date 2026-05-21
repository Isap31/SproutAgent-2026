import json
from pathlib import Path
from typing import Any


ROOT_DIR = Path(__file__).resolve().parents[1]
PROMPTS_DIR = ROOT_DIR / "prompts"


def load_prompt_template(template_name: str = "report_prompt.txt") -> str:
    """Load a prompt template from the prompts folder."""
    template_path = PROMPTS_DIR / template_name
    with template_path.open("r", encoding="utf-8") as file:
        return file.read()


def build_report_prompt(client_data: dict[str, Any], template_name: str = "report_prompt.txt") -> str:
    """Build the final consulting prompt for Gemini."""
    template = load_prompt_template(template_name)
    pretty_client_data = json.dumps(client_data, indent=2)
    return template.format(
        client_name=client_data.get("client_name", "Unknown Client"),
        client_data=pretty_client_data,
    )
