import json
import sys
from pathlib import Path

from src.client_registry import load_client_profile
from src.skills.source_mapping import map_epm_variance_export_to_monthly_board_package


DEFAULT_CLIENT_FOLDER = "coruscant-transit-bureau"
DEFAULT_EXPORT_PATH = Path(
    "clients/coruscant-transit-bureau/source_exports/sample_epm_variance_export.csv"
)
ROOT_DIR = Path(__file__).resolve().parents[1]


def get_workflow_output_path(client_folder: str) -> Path:
    """Return the Monthly Board Package workflow path for a client folder."""
    return ROOT_DIR / "clients" / client_folder / "workflows" / "monthly_board_package.json"


def should_write_workflow(args: list[str]) -> bool:
    """Return True if the command includes the --write flag."""
    return "--write" in args


def main() -> None:
    """Map an Oracle EPM-style source export into Monthly Board Package JSON.

    Usage:
      python3 -m src.map_source_export
      python3 -m src.map_source_export coruscant-transit-bureau clients/coruscant-transit-bureau/source_exports/sample_epm_variance_export.csv
      python3 -m src.map_source_export coruscant-transit-bureau clients/coruscant-transit-bureau/source_exports/sample_epm_variance_export.csv --write
    """
    args = [arg for arg in sys.argv[1:] if arg != "--write"]
    write_workflow = should_write_workflow(sys.argv[1:])

    client_folder = args[0] if len(args) > 0 else DEFAULT_CLIENT_FOLDER
    export_path = Path(args[1]) if len(args) > 1 else DEFAULT_EXPORT_PATH

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

    if write_workflow:
        output_path = get_workflow_output_path(client_folder)
        output_path.parent.mkdir(parents=True, exist_ok=True)
        output_path.write_text(json.dumps(workflow_data, indent=2), encoding="utf-8")
        print(f"Workflow file updated: {output_path}")
        print("Next command:")
        print(f"SPROUT_CLIENT_FOLDER={client_folder} SPROUT_OFFLINE_MODE=true python3 -m src.main")
        return

    print("\nMapped Monthly Board Package Data:")
    print(json.dumps(workflow_data, indent=2))
    print("\nTo write this mapped data into the client workflow file, rerun with --write.")


if __name__ == "__main__":
    main()
