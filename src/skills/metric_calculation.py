from typing import Any


def safe_divide(numerator: float, denominator: float) -> float:
    """Safely divide two numbers."""
    if denominator == 0:
        return 0.0
    return numerator / denominator


def calculate_monthly_board_metrics(data: dict[str, Any]) -> dict[str, Any]:
    """Calculate deterministic finance metrics for the Monthly Board Package skill."""
    financials = data["financials"]

    budget = float(financials["budget"])
    actuals = float(financials["actuals"])
    forecast = float(financials["forecast"])
    prior_month_actuals = float(financials["prior_month_actuals"])

    variance_amount = actuals - budget
    variance_percent = safe_divide(variance_amount, budget) * 100

    forecast_gap_amount = forecast - budget
    forecast_gap_percent = safe_divide(forecast_gap_amount, budget) * 100

    month_over_month_change = actuals - prior_month_actuals
    month_over_month_change_percent = safe_divide(
        month_over_month_change,
        prior_month_actuals,
    ) * 100

    return {
        "budget": round(budget, 2),
        "actuals": round(actuals, 2),
        "forecast": round(forecast, 2),
        "prior_month_actuals": round(prior_month_actuals, 2),
        "variance_amount": round(variance_amount, 2),
        "variance_percent": round(variance_percent, 2),
        "forecast_gap_amount": round(forecast_gap_amount, 2),
        "forecast_gap_percent": round(forecast_gap_percent, 2),
        "month_over_month_change": round(month_over_month_change, 2),
        "month_over_month_change_percent": round(month_over_month_change_percent, 2),
    }
