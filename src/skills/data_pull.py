import json
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


def load_monthly_board_package() -> dict[str, Any]:
    """Load mock data for the Monthly Board Package skill."""
    data = load_json_file("monthly_board_package.json")
    if not isinstance(data, dict):
        raise ValueError("monthly_board_package.json must contain a single JSON object.")
    return data
