import os
from pathlib import Path
from typing import Any

from src.agent import SproutAgent
from src.client_registry import list_client_folders
from src.main import load_local_env


ROOT_DIR = Path(__file__).resolve().parents[1]


def run_client(client_folder: str) -> dict[str, Any]:
    """Run the Monthly Board Package workflow for one client folder."""
    os.environ["SPROUT_CLIENT_FOLDER"] = client_folder
    os.environ.setdefault("SPROUT_OFFLINE_MODE", "true")

    agent = SproutAgent()
    return agent.run_monthly_board_package()


def main() -> None:
    """Run SproutAgent for every available client folder."""
    load_local_env()

    clients = list_client_folders()
    if not clients:
        print("No client folders found. Nothing to run.")
        return

    print("SproutAgent V1 Client Smoke Test")
    print("--------------------------------")
    print(f"Clients found: {len(clients)}")
    print("Mode: Offline fallback by default unless SPROUT_OFFLINE_MODE is already set")
    print("")

    results: list[dict[str, Any]] = []

    for client_folder in clients:
        print(f"Running client: {client_folder}")
        try:
            run_summary = run_client(client_folder)
            results.append(
                {
                    "client_folder": client_folder,
                    "client_name": run_summary.get("client_name"),
                    "status": "passed",
                    "output_path": str(run_summary.get("output_path")),
                    "run_log_path": str(run_summary.get("run_log_path")),
                }
            )
            print(f"  PASS: {run_summary.get('client_name')}")
            print(f"  Report: {run_summary.get('output_path')}")
            print(f"  Run log: {run_summary.get('run_log_path')}")
        except Exception as exc:  # noqa: BLE001
            results.append(
                {
                    "client_folder": client_folder,
                    "client_name": "unknown",
                    "status": "failed",
                    "error": str(exc),
                }
            )
            print(f"  FAIL: {exc}")
        print("")

    passed = sum(1 for result in results if result["status"] == "passed")
    failed = sum(1 for result in results if result["status"] == "failed")

    print("Smoke Test Summary")
    print("------------------")
    print(f"Passed: {passed}")
    print(f"Failed: {failed}")

    if failed:
        print("\nFailed clients:")
        for result in results:
            if result["status"] == "failed":
                print(f"- {result['client_folder']}: {result.get('error')}")
    else:
        print("\nAll client workflows completed successfully.")


if __name__ == "__main__":
    main()
