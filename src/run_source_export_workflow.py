import json
import os
import sys
from pathlib import Path

from src.agent import SproutAgent, format_run_summary
from src.client_registry import load_client_profile
from src.main import load_local_env, print_metric_summary
from src.map_source_export import get_workflow_output_path
from src.skills.source_export_validation import (
    format_validation_result,
    validate_epm_variance_export,
)
from src.skills.source_mapping import map_epm_variance_export_to_monthly_board_package


DEFAULT_CLIENT_FOLDER = "coruscant-transit-bureau"
DEFAULT_EXPORT_PATH = Path(
    "clients/coruscant-transit-bureau/source_exports/sample_epm_variance_export.csv"
)


def main() -> None:
    """Run the full source export workflow for one client.

    This command validates an Oracle EPM-style CSV export, maps it into the
    Monthly Board Package workflow JSON, writes the workflow file, then runs
    SproutAgent from that refreshed workflow data.
    """
    load_local_env()

    client_folder = sys.argv[1] if len(sys.argv) > 1 else DEFAULT_CLIENT_FOLDER
    export_path = Path(sys.argv[2]) if len(sys.argv) > 2 else DEFAULT_EXPORT_PATH

    os.environ["SPROUT_CLIENT_FOLDER"] = client_folder
    os.environ.setdefault("SPROUT_OFFLINE_MODE", "true")

    print("SproutAgent Source Export Workflow")
    print("----------------------------------")
    print(f"Client folder: {client_folder}")
    print(f"Source export: {export_path}")
    print("")

    validation_result = validate_epm_variance_export(export_path)
    print(format_validation_result(validation_result))
    if validation_result["status"] != "passed":
        raise SystemExit(1)

    print("\nMapping source export into Monthly Board Package workflow data...")
    client_profile = load_client_profile(client_folder)
    workflow_data = map_epm_variance_export_to_monthly_board_package(
        file_path=export_path,
        client_profile=client_profile,
    )

    workflow_output_path = get_workflow_output_path(client_folder)
    workflow_output_path.parent.mkdir(parents=True, exist_ok=True)
    workflow_output_path.write_text(json.dumps(workflow_data, indent=2), encoding="utf-8")
    print(f"Workflow file updated: {workflow_output_path}")

    print("\nRunning SproutAgent from refreshed workflow data...\n")
    agent = SproutAgent()
    run_summary = agent.run_monthly_board_package()

    print(format_run_summary(run_summary))
    print_metric_summary(run_summary["calculated_metrics"])

    report_folder = Path(str(run_summary["output_path"])).parent
    print("\nNext Steps")
    print("----------")
    print(f"Open this client's report folder: open {report_folder}")
    print("Review the Markdown report and JSON run log before treating the output as complete.")
    print("\nReminder: This output is a draft for human review.")


if __name__ == "__main__":
    main()
