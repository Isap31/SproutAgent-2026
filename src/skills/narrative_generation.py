import json
from typing import Any

from src.gemini_service import generate_with_gemini


def build_monthly_board_prompt(
    package_data: dict[str, Any],
    calculated_metrics: dict[str, Any],
) -> str:
    """Build the narrative prompt for the Monthly Board Package skill."""
    payload = {
        "package_data": package_data,
        "calculated_metrics": calculated_metrics,
    }

    return f"""
You are SproutAgent, a CFO and FP&A execution assistant for Orbital Horizons Consulting.

You are drafting a Monthly Board Package narrative using fictional practice data. The output is a first draft for human review.

Write in a professional CFO-ready tone. Focus on budget variance, forecast outlook, KPI performance, cost drivers, risks, and leadership decision points.

Return Markdown with these sections:

# Monthly Board Package Draft: {package_data.get('client_name', 'Client')}

## 1. Executive Summary
## 2. Budget vs. Actuals
## 3. Forecast Outlook
## 4. KPI Summary
## 5. Main Cost Drivers
## 6. Key Risks
## 7. Recommended Actions
## 8. CFO Decision Point
## 9. Human Review Notes

Use this structured data:
{json.dumps(payload, indent=2)}
""".strip()


def generate_monthly_board_narrative(
    package_data: dict[str, Any],
    calculated_metrics: dict[str, Any],
) -> str:
    """Generate CFO-ready narrative using Gemini."""
    prompt = build_monthly_board_prompt(package_data, calculated_metrics)
    return generate_with_gemini(prompt)
