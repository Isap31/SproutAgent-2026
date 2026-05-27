import os
import subprocess
import sys
from pathlib import Path

ROOT_DIR = Path(__file__).resolve().parents[1]
if str(ROOT_DIR) not in sys.path:
    sys.path.insert(0, str(ROOT_DIR))

import streamlit as st

from src.agent import SproutAgent, format_run_summary
from src.client_registry import list_client_folders, load_client_profile
from src.main import load_local_env
from src.skills.source_export_validation import (
    format_validation_result,
    validate_epm_variance_export,
)
from src.skills.source_mapping import map_epm_variance_export_to_monthly_board_package


def get_source_exports(client_folder: str) -> list[Path]:
    """Return available CSV source exports for a client."""
    export_dir = ROOT_DIR / "clients" / client_folder / "source_exports"
    if not export_dir.exists():
        return []
    return sorted(export_dir.glob("*.csv"))


def get_client_display_name(client_folder: str) -> str:
    """Return the friendly client name for a client folder."""
    try:
        profile = load_client_profile(client_folder)
    except Exception:  # noqa: BLE001
        return client_folder
    return profile.get("client_name", client_folder)


def open_report_folder(report_folder: Path) -> None:
    """Open a report folder in Finder on macOS."""
    subprocess.run(["open", str(report_folder)], check=False)


def run_source_export_demo(client_folder: str, export_path: Path) -> dict:
    """Validate, map, and run SproutAgent from a source export in memory."""
    load_local_env()
    os.environ["SPROUT_CLIENT_FOLDER"] = client_folder
    os.environ.setdefault("SPROUT_OFFLINE_MODE", "true")

    validation_result = validate_epm_variance_export(export_path)
    if validation_result["status"] != "passed":
        return {
            "validation_result": validation_result,
            "run_summary": None,
        }

    client_profile = load_client_profile(client_folder)
    workflow_data = map_epm_variance_export_to_monthly_board_package(
        file_path=export_path,
        client_profile=client_profile,
    )

    agent = SproutAgent()
    run_summary = agent.run_monthly_board_package(
        package_data=workflow_data,
        source_detail=f"In-memory source export mapping: {export_path}",
    )

    return {
        "validation_result": validation_result,
        "run_summary": run_summary,
    }


def main() -> None:
    """Run the SproutAgent local demo interface."""
    st.set_page_config(
        page_title="SproutAgent Demo",
        page_icon="🌱",
        layout="wide",
    )

    st.title("🌱 SproutAgent Local Demo")
    st.caption(
        "Mock Oracle EPM-style export → validation → in-memory mapping → "
        "Monthly Board Package draft → run log → human review"
    )

    st.info(
        "This local V1 demo uses mock data only. It demonstrates a controlled finance "
        "execution workflow, not a production Oracle EPM integration."
    )

    with st.expander("What this demo proves", expanded=True):
        st.markdown(
            """
            - A finance-system-style export can be validated before use.
            - Source data can be mapped into SproutAgent workflow data in memory.
            - The agent calculates financial metrics deterministically.
            - Draft commentary and reports are generated for human review.
            - Run logs preserve traceability.
            - Normal demo runs do not dirty Git or rewrite tracked workflow JSON.
            """
        )

    clients = list_client_folders()
    if not clients:
        st.error("No client folders found under clients/.")
        return

    client_display_lookup = {
        get_client_display_name(client_folder): client_folder for client_folder in clients
    }
    client_display_names = sorted(client_display_lookup.keys())

    with st.sidebar:
        st.header("Run Controls")
        selected_client_name = st.selectbox("Client", client_display_names)
        client_folder = client_display_lookup[selected_client_name]
        st.caption(f"Internal folder: `{client_folder}`")

        exports = get_source_exports(client_folder)

        if exports:
            export_labels = [str(path.relative_to(ROOT_DIR)) for path in exports]
            selected_export_label = st.selectbox("Source export", export_labels)
            selected_export = ROOT_DIR / selected_export_label
        else:
            selected_export = None
            st.warning("No CSV source exports found for this client.")

        offline_mode = st.checkbox("Offline fallback mode", value=True)
        os.environ["SPROUT_OFFLINE_MODE"] = "true" if offline_mode else "false"

        run_button = st.button("Run SproutAgent", type="primary", disabled=selected_export is None)

    st.subheader("Client Context")
    try:
        profile = load_client_profile(client_folder)
        st.markdown(f"**Client:** {profile.get('client_name', 'Unknown')}")
        st.markdown(f"**Industry:** {profile.get('industry', 'Unknown')}")
        st.markdown(f"**CFO Persona:** {profile.get('cfo_persona', 'CFO / FP&A leader')}")
        st.markdown(f"**Primary Finance Challenge:** {profile.get('primary_finance_challenge', 'No finance challenge provided.')}")
        st.markdown(f"**Transformation Goal:** {profile.get('transformation_goal', 'No transformation goal provided.')}")
    except Exception as exc:  # noqa: BLE001
        st.warning(f"Could not load client profile: {exc}")

    if selected_export:
        st.subheader("Selected Source Export")
        st.code(str(selected_export.relative_to(ROOT_DIR)))

        validation_preview = validate_epm_variance_export(selected_export)
        if validation_preview["status"] == "passed":
            st.success("Source export validation passed.")
        else:
            st.error("Source export validation failed.")
        with st.expander("View validation details"):
            st.text(format_validation_result(validation_preview))

    if run_button and selected_export:
        st.subheader("Run Result")
        with st.spinner("Running SproutAgent..."):
            result = run_source_export_demo(client_folder, selected_export)

        validation_result = result["validation_result"]
        run_summary = result["run_summary"]

        if validation_result["status"] != "passed":
            st.error("Run stopped because source export validation failed.")
            st.text(format_validation_result(validation_result))
            return

        if not run_summary:
            st.error("Run did not return a summary.")
            return

        st.success("SproutAgent run completed.")

        metrics = run_summary["calculated_metrics"]
        c1, c2, c3, c4 = st.columns(4)
        c1.metric("Budget", f"{metrics['budget']:,.0f}")
        c2.metric("Actuals", f"{metrics['actuals']:,.0f}")
        c3.metric("Variance", f"{metrics['variance_percent']:.2f}%")
        c4.metric("Forecast Gap", f"{metrics['forecast_gap_percent']:.2f}%")

        with st.expander("View run summary", expanded=True):
            st.text(format_run_summary(run_summary))

        report_path = Path(str(run_summary["output_path"]))
        report_folder = report_path.parent
        st.markdown(f"**Report path:** `{report_path}`")
        st.markdown(f"**Run log path:** `{run_summary['run_log_path']}`")

        if st.button("Open report folder"):
            open_report_folder(report_folder)

        st.warning("Reminder: This output is a draft for human review.")


if __name__ == "__main__":
    main()
