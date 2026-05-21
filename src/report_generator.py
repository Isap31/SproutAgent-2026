from datetime import datetime
from pathlib import Path


ROOT_DIR = Path(__file__).resolve().parents[1]
REPORTS_DIR = ROOT_DIR / "reports"


def slugify(value: str) -> str:
    """Create a simple file-safe slug."""
    return (
        value.lower()
        .replace(" ", "-")
        .replace("/", "-")
        .replace("_", "-")
    )


def save_report(client_name: str, report_markdown: str) -> Path:
    """Save a generated report as Markdown."""
    REPORTS_DIR.mkdir(parents=True, exist_ok=True)
    timestamp = datetime.now().strftime("%Y%m%d-%H%M%S")
    filename = f"{timestamp}-{slugify(client_name)}.md"
    output_path = REPORTS_DIR / filename
    output_path.write_text(report_markdown, encoding="utf-8")
    return output_path
