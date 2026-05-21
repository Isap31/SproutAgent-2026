import json
import os
from datetime import datetime
from pathlib import Path
from typing import Any


ROOT_DIR = Path(__file__).resolve().parents[2]
CLIENTS_DIR = ROOT_DIR / "clients"
RUNS_DIR = ROOT_DIR / "runs"


def make_json_safe(value: Any) -> Any:
    """Convert values like Path objects into JSON-safe values."""
    if isinstance(value, Path):
        return str(value)
    if isinstance(value, dict):
        return {key: make_json_safe(item) for key, item in value.items()}
    if isinstance(value, list):
        return [make_json_safe(item) for item in value]
    return value


def get_run_log_dir(client_folder: str, workflow_slug: str) -> Path:
    """Return the correct run log directory.

    Client-folder runs save logs under that client's reports workflow folder.
    Shared-data runs save logs in the root runs folder.
    """
    if client_folder and client_folder != "shared-data-default":
        return CLIENTS_DIR / client_folder / "reports" / workflow_slug / "run_logs"
    return RUNS_DIR


def save_run_log(run_summary: dict[str, Any]) -> Path:
    """Save an agent run summary as a JSON log."""
    workflow_slug = str(run_summary.get("workflow", "workflow")).lower().replace(" ", "_")
    client_folder = str(run_summary.get("client_folder", "shared-data-default"))
    timestamp = datetime.now().strftime("%Y%m%d-%H%M%S")

    log_dir = get_run_log_dir(client_folder, workflow_slug)
    log_dir.mkdir(parents=True, exist_ok=True)

    client_slug = str(run_summary.get("client_name", "client")).lower().replace(" ", "-")
    output_path = log_dir / f"{timestamp}-{client_slug}-{workflow_slug}-run-log.json"

    json_safe_summary = make_json_safe(run_summary)
    output_path.write_text(json.dumps(json_safe_summary, indent=2), encoding="utf-8")
    return output_path
