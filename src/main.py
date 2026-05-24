import os
from pathlib import Path

from src.agent import SproutAgent, format_run_summary
from src.client_registry import format_client_directory


def load_local_env() -> None:
    """Load simple KEY=VALUE pairs from a local .env file if one exists."""
    env_path = Path(__file__).resolve().parents[1] / ".env"
    if not env_path.exists():
        return

    for line in env_path.read_text(encoding="utf-8").splitlines():
        line = line.strip()
        if not line or line.startswith("#") or "=" not in line:
            continue
        key, value = line.split("=", 1)
        os.environ.setdefault(key.strip(), value.strip())


def print_metric_summary(metrics: dict) -> None:
    """Print a short metric summary for the terminal run."""
    print("\nMetric Summary")
    print("--------------")
    print(f"Budget: {metrics['budget']:,.2f}")
    print(f"Actuals: {metrics['actuals']:,.2f}")
    print(f"Variance: {metrics['variance_amount']:,.2f} ({metrics['variance_percent']:.2f}%)")
    print(f"Forecast: {metrics['forecast']:,.2f}")
    print(
        f"Forecast gap: {metrics['forecast_gap_amount']:,.2f} "
        f"({metrics['forecast_gap_percent']:.2f}%)"
    )


def print_next_steps(run_summary: dict) -> None:
    """Print helpful next-step commands after a successful run."""
    output_path = Path(str(run_summary["output_path"]))
    report_folder = output_path.parent

    print("\nNext Steps")
    print("----------")
    print(f"Open this client's report folder: open {report_folder}")
    print("Review the Markdown report and JSON run log before treating the output as complete.")


def main() -> None:
    """Run SproutAgent Phase 1 demo workflow."""
    load_local_env()

    offline_mode = os.getenv("SPROUT_OFFLINE_MODE", "false").lower() == "true"
    model_name = os.getenv("GEMINI_MODEL", "gemini-2.0-flash")
    selected_client_folder = os.getenv("SPROUT_CLIENT_FOLDER")

    print("SproutAgent Phase 1: Finance Execution Agent")
    print("Workflow: Monthly Board Package")
    print(f"AI mode: {'Offline fallback' if offline_mode else 'Gemini live with fallback'}")
    print(f"Configured model: {model_name}")

    if not selected_client_folder:
        print("\nNo SPROUT_CLIENT_FOLDER selected. Choose one available client folder:")
        print(format_client_directory())
        print("\nExample command:")
        print(
            "SPROUT_CLIENT_FOLDER=coruscant-transit-bureau "
            "SPROUT_OFFLINE_MODE=true python3 -m src.main"
        )
        print("\nAgent stopped safely. No report was generated.")
        return

    print(f"Selected client folder: {selected_client_folder}")
    print("Running agent...\n")

    agent = SproutAgent()
    run_summary = agent.run_monthly_board_package()

    print(format_run_summary(run_summary))
    print_metric_summary(run_summary["calculated_metrics"])
    print_next_steps(run_summary)
    print("\nReminder: This output is a draft for human review.")


if __name__ == "__main__":
    main()
