import json
import os
from pathlib import Path
from typing import Any


ROOT_DIR = Path(__file__).resolve().parents[2]
DATA_DIR = ROOT_DIR / "data"
CLIENTS_DIR = ROOT_DIR / "clients"


def load_json_path(file_path: Path) -> dict[str, Any] | list[dict[str, Any]]:
    """Load a JSON file from an exact path."""
    if not file_path.exists():
        raise FileNotFoundError(f"Data file not found: {file_path}")

    with file_path.open("r", encoding="utf-8") as file:
        return json.load(file)


def load_json_file(filename: str) -> dict[str, Any] | list[dict[str, Any]]:
    """Load a JSON file from the shared data folder."""
    return load_json_path(DATA_DIR / filename)


def load_client_workflow_file(client_folder: str, workflow_file: str) -> dict[str, Any]:
    """Load workflow data from a specific client folder."""
    file_path = CLIENTS_DIR / client_folder / workflow_file
    data = load_json_path(file_path)
    if not isinstance(data, dict):
        raise ValueError(f"{file_path} must contain a single JSON object.")
    return data


def load_monthly_board_packages() -> list[dict[str, Any]]:
    """Load all mock data records for the Monthly Board Package skill."""
    data = load_json_file("monthly_board_package.json")
    if isinstance(data, dict):
        return [data]
    if isinstance(data, list):
        return data
    raise ValueError("monthly_board_package.json must contain a JSON object or list.")


def load_monthly_board_package(client_id: str | None = None) -> dict[str, Any]:
    """Load one mock Monthly Board Package record.

    Priority order:
    1. SPROUT_CLIENT_FOLDER from clients/<folder>/monthly_board_package.json
    2. client_id argument or SPROUT_CLIENT_ID from shared data/monthly_board_package.json
    3. first package in shared data file
    """
    client_folder = os.getenv("SPROUT_CLIENT_FOLDER")
    if client_folder:
        return load_client_workflow_file(client_folder, "monthly_board_package.json")

    packages = load_monthly_board_packages()
    selected_client_id = client_id or os.getenv("SPROUT_CLIENT_ID")

    if not selected_client_id:
        return packages[0]

    for package in packages:
        if package.get("client_id") == selected_client_id:
            return package

    available = ", ".join(package.get("client_id", "unknown") for package in packages)
    raise ValueError(
        f"Client id '{selected_client_id}' was not found. Available clients: {available}"
    )
