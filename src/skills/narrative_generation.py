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


def build_fallback_monthly_board_narrative(
    package_data: dict[str, Any],
    calculated_metrics: dict[str, Any],
    error_message: str,
) -> str:
    """Create a deterministic fallback report when Gemini is unavailable."""
    client_name = package_data.get("client_name", "Unknown Client")
    reporting_month = package_data.get("reporting_month", "Unknown Period")
    kpis = package_data.get("kpis", {})
    cost_drivers = package_data.get("cost_drivers", [])
    risks = package_data.get("risks", [])

    return f"""# Monthly Board Package Draft: {client_name}

## 1. Executive Summary

{client_name} is reporting an unfavorable budget variance for {reporting_month}. Actual spend is above budget, and the forecast suggests continued cost pressure if corrective action is not taken. This fallback report was generated without live AI narrative generation because the Gemini API was unavailable.

## 2. Budget vs. Actuals

- Budget: {calculated_metrics['budget']:,.2f}
- Actuals: {calculated_metrics['actuals']:,.2f}
- Variance amount: {calculated_metrics['variance_amount']:,.2f}
- Variance percent: {calculated_metrics['variance_percent']:.2f}%
- Prior month actuals: {calculated_metrics['prior_month_actuals']:,.2f}
- Month-over-month change: {calculated_metrics['month_over_month_change']:,.2f}

## 3. Forecast Outlook

- Forecast: {calculated_metrics['forecast']:,.2f}
- Forecast gap to budget: {calculated_metrics['forecast_gap_amount']:,.2f}
- Forecast gap percent: {calculated_metrics['forecast_gap_percent']:.2f}%

The current forecast indicates that leadership should review cost controls, operating assumptions, and near-term mitigation options.

## 4. KPI Summary

{json.dumps(kpis, indent=2)}

## 5. Main Cost Drivers

{chr(10).join(f'- {driver}' for driver in cost_drivers)}

## 6. Key Risks

{chr(10).join(f'- {risk}' for risk in risks)}

## 7. Recommended Actions

- Review the largest cost drivers and confirm whether they are one-time or recurring.
- Validate forecast assumptions with the operating team.
- Identify near-term cost controls that do not harm service reliability.
- Create a leadership review package for the next reporting cycle.

## 8. CFO Decision Point

The CFO should decide whether to approve a targeted cost-control review focused on the largest variance drivers and forecast risks.

## 9. Human Review Notes

- This is a deterministic fallback draft.
- Gemini narrative generation was unavailable.
- Error summary: {error_message}
- A human reviewer should validate all financial numbers, assumptions, and recommendations before use.
"""


def generate_monthly_board_narrative(
    package_data: dict[str, Any],
    calculated_metrics: dict[str, Any],
) -> str:
    """Generate CFO-ready narrative using Gemini, with deterministic fallback."""
    prompt = build_monthly_board_prompt(package_data, calculated_metrics)
    try:
        return generate_with_gemini(prompt)
    except Exception as exc:  # noqa: BLE001
        return build_fallback_monthly_board_narrative(
            package_data=package_data,
            calculated_metrics=calculated_metrics,
            error_message=str(exc),
        )
