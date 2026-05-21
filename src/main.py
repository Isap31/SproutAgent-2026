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


def main() -> None:
    """Run SproutAgent Phase 1 demo workflow."""
    load_local_env()

    print("SproutAgent Phase 1: Finance Execution Agent")
    print("Running Monthly Board Package workflow...")

    orchestrator = SproutAgentOrchestrator()
    output_path = orchestrator.run_monthly_board_package()

    print(f"Draft report created: {output_path}")
    print("Reminder: This output is a draft for human review.")


if __name__ == "__main__":
    main()
