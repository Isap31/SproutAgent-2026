from typing import Any


class ValidationError(ValueError):
    """Raised when required finance reporting data is missing."""


def validate_required_fields(data: dict[str, Any], required_fields: list[str]) -> None:
    """Validate that top-level required fields exist and are not empty."""
    missing = [field for field in required_fields if data.get(field) in (None, "", [])]
    if missing:
        raise ValidationError(f"Missing required fields: {', '.join(missing)}")


def validate_monthly_board_package(data: dict[str, Any]) -> None:
    """Validate the minimum inputs needed for the Monthly Board Package skill."""
    validate_required_fields(
        data,
        [
            "client_id",
            "client_name",
            "reporting_month",
            "package_type",
            "financials",
            "kpis",
            "cost_drivers",
            "risks",
        ],
    )

    financials = data.get("financials", {})
    required_financials = ["budget", "actuals", "forecast", "prior_month_actuals"]
    missing_financials = [field for field in required_financials if financials.get(field) is None]
    if missing_financials:
        raise ValidationError(
            f"Missing required financial fields: {', '.join(missing_financials)}"
        )

    if financials["budget"] <= 0:
        raise ValidationError("Budget must be greater than zero.")
