import json
from pathlib import Path
from typing import Any


ROOT_DIR = Path(__file__).resolve().parents[1]
DATA_DIR = ROOT_DIR / "data"


def load_planets() -> list[dict[str, Any]]:
    """Load mock planetary client profiles."""
    planets_path = DATA_DIR / "planets.json"
    with planets_path.open("r", encoding="utf-8") as file:
        return json.load(file)


def get_client_by_id(client_id: str) -> dict[str, Any]:
    """Return one client profile by its id."""
    clients = load_planets()
    for client in clients:
        if client.get("id") == client_id:
            return client
    available = ", ".join(client.get("id", "unknown") for client in clients)
    raise ValueError(f"Client id '{client_id}' was not found. Available clients: {available}")


def list_client_options() -> list[str]:
    """Return all available mock client ids."""
    return [client["id"] for client in load_planets()]
