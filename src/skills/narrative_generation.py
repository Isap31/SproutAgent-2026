import json
import os
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
## 2. Financial Performance Snapshot
## 3. Budget vs. Actuals
## 4. Forecast Outlook
## 5. KPI Commentary
## 6. Main Cost Drivers
## 7. Key Risks
## 8. Recommended Actions
## 9. CFO Decision Point
## 10. Human Review Notes

Use this structured data:
{json.dumps(payload, indent=2)}
""".strip()


def format_bullet_list(items: list[Any], empty_message: str) -> str:
    """Format a list as Markdown bullets."""
    if not items:
        return f"- {empty_message}"
    return "\n".join(f"- {item}" for item in items)


def format_kpi_commentary(kpis: dict[str, Any]) -> str:
    """Create readable KPI commentary from structured KPI values."""
    if not kpis:
        return "- No KPI values were provided in the source workflow data."

    lines = []
    for name, value in kpis.items():
        readable_name = name.replace("_", " ").title()
        if isinstance(value, float) and 0 <= value <= 1:
            lines.append(f"- {readable_name}: {value:.1%}")
        elif isinstance(value, (int, float)):
            lines.append(f"- {readable_name}: {value:,.2f}")
        else:
            lines.append(f"- {readable_name}: {value}")
    return "\n".join(lines)


def get_variance_assessment(variance_percent: float) -> str:
    """Return a CFO-ready variance assessment based on materiality."""
    abs_variance = abs(variance_percent)
    if abs_variance >= 20:
        return "critical variance requiring immediate leadership attention"
    if abs_variance >= 10:
        return "material variance requiring management review"
    if abs_variance >= 5:
        return "moderate variance requiring monitoring"
    return "minor variance within a normal monitoring range"


def build_fallback_monthly_board_narrative(
    package_data: dict[str, Any],
    calculated_metrics: dict[str, Any],
    error_message: str,
) -> str:
    """Create a deterministic fallback report when Gemini is unavailable."""
    client_name = package_data.get("client_name", "Unknown Client")
    reporting_month = package_data.get("reporting_month", "Unknown Period")
    cfo_persona = package_data.get("cfo_persona", "CFO / FP&A leader")
    kpis = package_data.get("kpis", {})
    cost_drivers = package_data.get("cost_drivers", [])
    leadership_notes = package_data.get("leadership_notes", [])
    risks = package_data.get("risks", [])

    variance_percent = calculated_metrics["variance_percent"]
    forecast_gap_percent = calculated_metrics["forecast_gap_percent"]
    variance_assessment = get_variance_assessment(variance_percent)

    return f"""# Monthly Board Package Draft: {client_name}

## 1. Executive Summary

{client_name} is reporting a {variance_assessment} for {reporting_month}. Actual spend is {variance_percent:.2f}% above budget, with a forecast gap of {forecast_gap_percent:.2f}% to budget. The current profile suggests that leadership should focus on the largest cost drivers, confirm whether the variance is temporary or recurring, and decide what mitigation actions should be prioritized before the next reporting cycle.

The intended reviewer is a {cfo_persona}. This draft is structured to support CFO and FP&A review, not to replace final judgment.

## 2. Financial Performance Snapshot

| Metric | Value |
|---|---:|
| Budget | {calculated_metrics['budget']:,.2f} |
| Actuals | {calculated_metrics['actuals']:,.2f} |
| Variance Amount | {calculated_metrics['variance_amount']:,.2f} |
| Variance Percent | {calculated_metrics['variance_percent']:.2f}% |
| Forecast | {calculated_metrics['forecast']:,.2f} |
| Forecast Gap to Budget | {calculated_metrics['forecast_gap_amount']:,.2f} |
| Forecast Gap Percent | {calculated_metrics['forecast_gap_percent']:.2f}% |
| Prior Month Actuals | {calculated_metrics['prior_month_actuals']:,.2f} |
| Month-over-Month Change | {calculated_metrics['month_over_month_change']:,.2f} |
| Month-over-Month Change Percent | {calculated_metrics['month_over_month_change_percent']:.2f}% |

## 3. Budget vs. Actuals

Actuals are above budget by {calculated_metrics['variance_amount']:,.2f}, representing an unfavorable variance of {calculated_metrics['variance_percent']:.2f}%. This level of variance should be reviewed with the operating owners tied to the largest cost drivers. The immediate question for leadership is whether the variance reflects timing, one-time disruption, or a structural run-rate issue.

## 4. Forecast Outlook

The current forecast is {calculated_metrics['forecast']:,.2f}, which is {calculated_metrics['forecast_gap_amount']:,.2f} above budget. This creates a forecast gap of {calculated_metrics['forecast_gap_percent']:.2f}% and indicates that current operating assumptions may not be aligned with the original plan.

Recommended forecast review focus:

- Confirm whether current cost pressure is expected to continue.
- Revisit assumptions behind the largest cost categories.
- Identify mitigation actions that can be taken before the next reporting cycle.
- Separate one-time items from recurring run-rate pressure.

## 5. KPI Commentary

{format_kpi_commentary(kpis)}

These KPIs should be reviewed alongside the financial variance so leadership can connect performance trends to cost behavior.

## 6. Main Cost Drivers

{format_bullet_list(cost_drivers, 'No cost drivers were provided in the source workflow data.')}

The cost driver review should focus on ownership, controllability, and whether each driver is expected to continue into the next period.

## 7. Leadership Notes

{format_bullet_list(leadership_notes, 'No leadership notes were provided in the source workflow data.')}

## 8. Key Risks

{format_bullet_list(risks, 'No risks were provided in the source workflow data.')}

## 9. Recommended Actions

- Confirm the top two to three drivers behind the unfavorable variance.
- Validate whether the forecast gap is caused by timing, volume, rate, or operational disruption.
- Assign an owner to each major mitigation action.
- Prepare a follow-up view for leadership showing revised forecast assumptions.
- Keep the report in draft status until a CFO, FP&A professional, or consultant completes review.

## 10. CFO Decision Point

The CFO should decide whether to initiate a targeted variance review and mitigation plan for the largest cost drivers. The decision should focus on whether the current forecast requires immediate corrective action or whether the variance can be managed through monitoring and normal operating controls.

## 11. Human Review Notes

- This is a deterministic fallback draft generated without live AI narrative completion.
- The report was produced from structured source data and calculated metrics.
- Mode or error summary: {error_message}
- A human reviewer should validate all financial numbers, business assumptions, and recommendations before use.
"""


def generate_monthly_board_narrative(
    package_data: dict[str, Any],
    calculated_metrics: dict[str, Any],
) -> str:
    """Generate CFO-ready narrative using Gemini, with deterministic fallback."""
    offline_mode = os.getenv("SPROUT_OFFLINE_MODE", "false").lower() == "true"

    if offline_mode:
        return build_fallback_monthly_board_narrative(
            package_data=package_data,
            calculated_metrics=calculated_metrics,
            error_message="Local offline mode enabled. Gemini was bypassed for this test run.",
        )

    prompt = build_monthly_board_prompt(package_data, calculated_metrics)

    try:
        return generate_with_gemini(prompt)
    except Exception as exc:  # noqa: BLE001
        return build_fallback_monthly_board_narrative(
            package_data=package_data,
            calculated_metrics=calculated_metrics,
            error_message=str(exc),
        )
