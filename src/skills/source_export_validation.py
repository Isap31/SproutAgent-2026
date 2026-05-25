import csv
from pathlib import Path
from typing import Any


REQUIRED_EPM_VARIANCE_COLUMNS = [
    "account",
    "entity",
    "scenario",
    "period",
    "budget",
    "actuals",
    "forecast",
    "prior_month_actuals",
    "kpi_name",
    "kpi_value",
    "cost_driver",
    "risk_indicator",
    "leadership_note",
]

NUMERIC_COLUMNS = [
    "budget",
    "actuals",
    "forecast",
    "prior_month_actuals",
]


def read_csv_rows(file_path: Path) -> list[dict[str, str]]:
    """Read a CSV export into a list of dictionaries."""
    if not file_path.exists():
        raise FileNotFoundError(f"Source export not found: {file_path}")

    with file_path.open("r", encoding="utf-8-sig", newline="") as file:
        reader = csv.DictReader(file)
        return list(reader)


def get_missing_columns(actual_columns: list[str], required_columns: list[str]) -> list[str]:
    """Return required columns that are missing from the export."""
    actual_column_set = set(actual_columns)
    return [column for column in required_columns if column not in actual_column_set]


def validate_numeric_value(value: str) -> bool:
    """Return True when a value can be interpreted as a number."""
    try:
        float(value)
    except (TypeError, ValueError):
        return False
    return True


def validate_epm_variance_export(file_path: str | Path) -> dict[str, Any]:
    """Validate an Oracle EPM-style variance export CSV.

    This does not connect to Oracle EPM. It validates the local CSV shape that
    future EPM exports are expected to follow before mapping into SproutAgent
    workflow data.
    """
    path = Path(file_path)
    rows = read_csv_rows(path)

    if not rows:
        return {
            "status": "failed",
            "file_path": str(path),
            "rows_checked": 0,
            "missing_columns": REQUIRED_EPM_VARIANCE_COLUMNS,
            "numeric_errors": [],
            "message": "The source export is empty or has no data rows.",
            "ready_for_mapping": False,
        }

    actual_columns = list(rows[0].keys())
    missing_columns = get_missing_columns(actual_columns, REQUIRED_EPM_VARIANCE_COLUMNS)

    numeric_errors = []
    if not missing_columns:
        for row_number, row in enumerate(rows, start=2):
            for column in NUMERIC_COLUMNS:
                if not validate_numeric_value(row.get(column, "")):
                    numeric_errors.append(
                        {
                            "row": row_number,
                            "column": column,
                            "value": row.get(column, ""),
                        }
                    )

    status = "passed" if not missing_columns and not numeric_errors else "failed"

    return {
        "status": status,
        "file_path": str(path),
        "rows_checked": len(rows),
        "required_columns": REQUIRED_EPM_VARIANCE_COLUMNS,
        "actual_columns": actual_columns,
        "missing_columns": missing_columns,
        "numeric_errors": numeric_errors,
        "ready_for_mapping": status == "passed",
    }


def format_validation_result(result: dict[str, Any]) -> str:
    """Format source export validation result for terminal output."""
    lines = [
        "Source Export Validation",
        "------------------------",
        f"File: {result.get('file_path')}",
        f"Status: {str(result.get('status')).upper()}",
        f"Rows checked: {result.get('rows_checked')}",
        f"Ready for mapping: {result.get('ready_for_mapping')}",
    ]

    missing_columns = result.get("missing_columns", [])
    numeric_errors = result.get("numeric_errors", [])

    if missing_columns:
        lines.append("\nMissing columns:")
        for column in missing_columns:
            lines.append(f"- {column}")

    if numeric_errors:
        lines.append("\nNumeric validation errors:")
        for error in numeric_errors:
            lines.append(
                f"- Row {error['row']}, column {error['column']}: {error['value']}"
            )

    if result.get("ready_for_mapping"):
        lines.append("\nThe export has the required shape for the future mapping layer.")
    else:
        lines.append("\nFix the export before using it as a SproutAgent source file.")

    return "\n".join(lines)
