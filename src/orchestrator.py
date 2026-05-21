from pathlib import Path
from typing import Any

from src.skills.data_pull import load_monthly_board_package
from src.skills.metric_calculation import calculate_monthly_board_metrics
from src.skills.narrative_generation import generate_monthly_board_narrative
from src.skills.output_generation import save_monthly_board_package
from src.skills.validation import validate_monthly_board_package


class SproutAgentOrchestrator:
    """Phase 1 Finance Execution Agent orchestrator.

    This orchestrator does not act autonomously. It runs a controlled,
    repeatable finance reporting workflow using deterministic skills first,
    then AI narrative generation, then human-review-ready output.
    """

    def run_monthly_board_package(self) -> dict[str, Any]:
        """Run the Monthly Board Package skill end-to-end."""
        package_data = load_monthly_board_package()
        validate_monthly_board_package(package_data)
        calculated_metrics = calculate_monthly_board_metrics(package_data)
        narrative = generate_monthly_board_narrative(package_data, calculated_metrics)
        output_path = save_monthly_board_package(package_data, narrative)

        return {
            "client_name": package_data.get("client_name", "Unknown Client"),
            "reporting_month": package_data.get("reporting_month", "Unknown Period"),
            "output_path": output_path,
            "calculated_metrics": calculated_metrics,
        }
