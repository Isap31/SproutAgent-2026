import os
from datetime import datetime
from pathlib import Path
from typing import Any

from src.orchestrator import SproutAgentOrchestrator
from src.skills.run_logging import save_run_log


class SproutAgent:
    """Controlled finance execution agent for CFO and FP&A workflows.

    SproutAgent is intentionally not autonomous. It coordinates approved
    workflows, records execution steps, and keeps human review visible.
    """

    def __init__(self) -> None:
        self.orchestrator = SproutAgentOrchestrator()
        self.steps: list[dict[str, str]] = []

    def record_step(self, name: str, status: str, detail: str = "") -> None:
        """Record a step in the agent run."""
        self.steps.append(
            {
                "step": name,
                "status": status,
                "detail": detail,
            }
        )

    def run_monthly_board_package(self) -> dict[str, Any]:
        """Run the Monthly Board Package workflow and return a run summary."""
        started_at = datetime.now().isoformat(timespec="seconds")
        requested_client_folder = os.getenv("SPROUT_CLIENT_FOLDER", "shared-data-default")
        offline_mode = os.getenv("SPROUT_OFFLINE_MODE", "false").lower() == "true"
        ai_mode = "Offline fallback" if offline_mode else "Gemini live with fallback"

        self.record_step(
            "Agent initialized",
            "completed",
            f"Requested client folder: {requested_client_folder}",
        )
        self.record_step(
            "Workflow selected",
            "completed",
            "Monthly Board Package",
        )

        result = self.orchestrator.run_monthly_board_package()

        self.record_step(
            "Client workflow data loaded",
            "completed",
            result.get("client_name", "Unknown Client"),
        )
        self.record_step(
            "Validation completed",
            "completed",
            "Required finance fields were present.",
        )
        self.record_step(
            "Metrics calculated",
            "completed",
            "Budget, actuals, variance, forecast, and forecast gap calculated.",
        )
        self.record_step(
            "Narrative generated",
            "completed",
            ai_mode,
        )
        self.record_step(
            "Report saved",
            "completed",
            str(result.get("output_path")),
        )
        self.record_step(
            "Human review required",
            "required",
            "A CFO, FP&A professional, or consultant must review the draft.",
        )

        completed_at = datetime.now().isoformat(timespec="seconds")

        run_summary = {
            "agent_name": "SproutAgent",
            "workflow": "Monthly Board Package",
            "client_name": result.get("client_name"),
            "reporting_month": result.get("reporting_month"),
            "client_folder": requested_client_folder,
            "ai_mode": ai_mode,
            "status": "completed",
            "started_at": started_at,
            "completed_at": completed_at,
            "output_path": result.get("output_path"),
            "calculated_metrics": result.get("calculated_metrics"),
            "human_review_required": True,
            "steps": self.steps,
        }

        run_log_path = save_run_log(run_summary)
        self.record_step("Run log saved", "completed", str(run_log_path))
        run_summary["run_log_path"] = run_log_path
        run_summary["steps"] = self.steps

        return run_summary


def format_run_summary(run_summary: dict[str, Any]) -> str:
    """Format an agent run summary for terminal output."""
    output_path = run_summary.get("output_path")
    if isinstance(output_path, Path):
        output_path = str(output_path)

    run_log_path = run_summary.get("run_log_path")
    if isinstance(run_log_path, Path):
        run_log_path = str(run_log_path)

    lines = [
        "SproutAgent Run Summary",
        "------------------------",
        f"Status: {run_summary.get('status')}",
        f"Client: {run_summary.get('client_name')}",
        f"Client folder: {run_summary.get('client_folder')}",
        f"Workflow: {run_summary.get('workflow')}",
        f"Reporting period: {run_summary.get('reporting_month')}",
        f"AI mode: {run_summary.get('ai_mode')}",
        f"Output: {output_path}",
        f"Run log: {run_log_path}",
        f"Human review required: {run_summary.get('human_review_required')}",
        "",
        "Execution Steps:",
    ]

    for step in run_summary.get("steps", []):
        lines.append(f"- {step['status'].upper()}: {step['step']} — {step['detail']}")

    return "\n".join(lines)
