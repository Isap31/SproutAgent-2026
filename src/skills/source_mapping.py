from pathlib import Path
from typing import Any

from src.skills.source_export_validation import read_csv_rows, validate_epm_variance_export


def parse_number(value: str) -> float:
    """Parse a numeric CSV value into a float."""
    return float(value)


def unique_non_empty(values: list[str]) -> list[str]:
    """Return unique non-empty values while preserving order."""
    seen = set()
    output = []
    for value in values:
        clean_value = value.strip()
        if clean_value and clean_value not in seen:
            seen.add(clean_value)
            output.append(clean_value)
    return output


def map_epm_variance_export_to_monthly_board_package(
    file_path: str | Path,
    client_profile: dict[str, Any],
) -> dict[str, Any]:
    """Map an Oracle EPM-style variance export into Monthly Board Package data."""
    validation_result = validate_epm_variance_export(file_path)
    if validation_result["status"] != "passed":
        raise ValueError(
            "Source export failed validation and cannot be mapped. "
            f"Result: {validation_result}"
        )

    rows = read_csv_rows(Path(file_path))
    first_row = rows[0]

    budget = sum(parse_number(row["budget"]) for row in rows)
    actuals = sum(parse_number(row["actuals"]) for row in rows)
    forecast = sum(parse_number(row["forecast"]) for row in rows)
    prior_month_actuals = sum(parse_number(row["prior_month_actuals"]) for row in rows)

    kpis = {}
    for row in rows:
        kpi_name = row.get("kpi_name", "").strip()
        kpi_value = row.get("kpi_value", "").strip()
        if not kpi_name or not kpi_value:
            continue
        try:
            kpis[kpi_name] = parse_number(kpi_value)
        except ValueError:
            kpis[kpi_name] = kpi_value

    return {
        "client_id": client_profile.get("client_id", "unknown-client"),
        "client_name": client_profile.get("client_name", "Unknown Client"),
        "cfo_persona": client_profile.get("cfo_persona", "CFO / FP&A leader"),
        "reporting_month": first_row.get("period", "Unknown Period"),
        "package_type": "Monthly Board Package",
        "source_system": "Oracle EPM-style export",
        "source_file": str(file_path),
        "source_scenario": first_row.get("scenario", "Unknown Scenario"),
        "source_entity": first_row.get("entity", "Unknown Entity"),
        "financials": {
            "budget": budget,
            "actuals": actuals,
            "forecast": forecast,
            "prior_month_actuals": prior_month_actuals,
        },
        "kpis": kpis,
        "cost_drivers": unique_non_empty([row.get("cost_driver", "") for row in rows]),
        "leadership_notes": unique_non_empty(
            [row.get("leadership_note", "") for row in rows]
        ),
        "risks": unique_non_empty([row.get("risk_indicator", "") for row in rows]),
    }
