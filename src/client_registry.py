import json
from pathlib import Path
from typing import Any


ROOT_DIR = Path(__file__).resolve().parents[1]
CLIENTS_DIR = ROOT_DIR / "clients"


def list_client_folders() -> list[str]:
    """Return available client folder names."""
    if not CLIENTS_DIR.exists():
        return []

    return sorted(
        item.name
        for item in CLIENTS_DIR.iterdir()
        if item.is_dir() and not item.name.startswith(".")
    )


def load_client_profile(client_folder: str) -> dict[str, Any]:
    """Load a client profile from clients/<client_folder>/client_profile.json."""
    profile_path = CLIENTS_DIR / client_folder / "client_profile.json"
    if not profile_path.exists():
        return {
            "client_id": client_folder,
            "client_name": client_folder,
            "cfo_persona": "No client profile found.",
        }

    with profile_path.open("r", encoding="utf-8") as file:
        return json.load(file)


def list_client_profiles() -> list[dict[str, Any]]:
    """Return profiles for all available client folders."""
    profiles = []
    for client_folder in list_client_folders():
        profile = load_client_profile(client_folder)
        profile["client_folder"] = client_folder
        profiles.append(profile)
    return profiles


def format_client_directory() -> str:
    """Format available clients for terminal display."""
    profiles = list_client_profiles()
    if not profiles:
        return "No client folders found."

    lines = [
        "Available Client Folders",
        "------------------------",
    ]

    for profile in profiles:
        lines.append(f"- {profile.get('client_folder')}: {profile.get('client_name')}")
        lines.append(f"  CFO focus: {profile.get('cfo_persona', 'Not provided')}")

    return "\n".join(lines)
