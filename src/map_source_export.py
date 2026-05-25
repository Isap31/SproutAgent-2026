import json
import sys
from pathlib import Path

from src.client_registry import load_client_profile
from src.skills.source_mapping import map_epm_variance_export_to_monthly_board_package


DEFAULT_CLIENT_FOLDER = "coruscant-transit-bureau"
DEFAULT_EXPORT_PATH = Path(
    "clients/coruscant-transit-bureau/source_exports/sample_epm_variance_export.csv"
)


def main() -> None:
    """Map an Oracle EPM-style source export into Monthly Board Package JSON."""
    client_folder = sys.argv[1] if len(sys.argv) > 1 else DEFAULT_CLIENT_FOLDER
    export_path = Path(sys.argv[2]) if len(sys.argv) > 2 else DEFAULT_EXPORT_PATH

    client_profile = load_client_profile(client_folder)
    workflow_data = map_epm_variance_export_to_monthly_board_package(
        file_path=export_path,
        client_profile=client_profile,
    )

    print("Source Export Mapping")
    print("---------------------")
    print(f"Client folder: {client_folder}")
    print(f"Source export: {export_path}")
    print("Status: PASSED")
    print("\nMapped Monthly Board Package Data:")
    print(json.dumps(workflow_data, indent=2))


if __name__ == "__main__":
    main()
