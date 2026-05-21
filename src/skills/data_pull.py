import json
import os
from pathlib import Path
from typing import Any


ROOT_DIR = Path(__file__).resolve().parents[2]
DATA_DIR = ROOT_DIR / "data"


def load_json_file(filename: str) -> dict[str, Any] | list[dict[str, Any]]:
    """Load a JSON file from the data folder."""
    file_path = DATA_DIR / filename
    if not file_path.exists():
        raise FileNotFoundError(f"Data file not found: {file_path}")

    with file_path.open("r", encoding="utf-8") as file:
        return json.load(file)


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

    If no client_id is provided, this function uses SPROUT_CLIENT_ID from the
    environment. If neither is set, the first package is returned.
    """
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
