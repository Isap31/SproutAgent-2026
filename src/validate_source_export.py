import sys
from pathlib import Path

from src.skills.source_export_validation import (
    format_validation_result,
    validate_epm_variance_export,
)


DEFAULT_EXPORT_PATH = Path(
    "clients/coruscant-transit-bureau/source_exports/sample_epm_variance_export.csv"
)


def main() -> None:
    """Validate an Oracle EPM-style source export CSV."""
    export_path = Path(sys.argv[1]) if len(sys.argv) > 1 else DEFAULT_EXPORT_PATH
    result = validate_epm_variance_export(export_path)
    print(format_validation_result(result))

    if result["status"] != "passed":
        raise SystemExit(1)


if __name__ == "__main__":
    main()
