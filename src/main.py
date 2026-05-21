import os
from pathlib import Path

from src.orchestrator import SproutAgentOrchestrator


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


def main() -> None:
    """Run SproutAgent Phase 1 demo workflow."""
    load_local_env()

    offline_mode = os.getenv("SPROUT_OFFLINE_MODE", "false").lower() == "true"
    model_name = os.getenv("GEMINI_MODEL", "gemini-2.0-flash")

    print("SproutAgent Phase 1: Finance Execution Agent")
    print("Workflow: Monthly Board Package")
    print(f"AI mode: {'Offline fallback' if offline_mode else 'Gemini live with fallback'}")
    print(f"Configured model: {model_name}")
    print("Running workflow...\n")

    orchestrator = SproutAgentOrchestrator()
    result = orchestrator.run_monthly_board_package()

    print("Workflow complete.")
    print(f"Client: {result['client_name']}")
    print(f"Reporting period: {result['reporting_month']}")
    print_metric_summary(result["calculated_metrics"])
    print(f"\nDraft report created: {result['output_path']}")
    print("Reminder: This output is a draft for human review.")


if __name__ == "__main__":
    main()
