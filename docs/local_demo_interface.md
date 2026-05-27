# Local Demo Interface

This guide explains how to run the SproutAgent local Streamlit demo interface.

## Purpose

The local demo interface gives SproutAgent a simple visual workflow for V1.

It is not a production app and it is not a live Oracle EPM integration. It is a local demonstration of the controlled finance execution workflow.

## What The Demo Shows

```text
Mock Oracle EPM-style CSV export
↓
Source export validation
↓
In-memory source mapping
↓
SproutAgent Monthly Board Package run
↓
Markdown report output
↓
JSON run log
↓
Human review
```

## Launch Command

From the project root:

```bash
cd /Users/caitlinprzywara3/Desktop/SproutAgent-2026
streamlit run src/demo_app.py
```

If Streamlit is not installed locally yet, run:

```bash
pip3 install streamlit
```

## Current Demo Controls

The sidebar currently supports:

- Selecting a client folder
- Selecting a source export CSV
- Running in offline fallback mode
- Running SproutAgent from the selected export

## Current Default Demo Path

The current default demo uses:

```text
Client: coruscant-transit-bureau
Source export: clients/coruscant-transit-bureau/source_exports/sample_epm_variance_export.csv
Workflow: Monthly Board Package
Mode: Offline fallback
```

## Expected Result

After clicking **Run SproutAgent**, the app should show:

- validation passed
- run completed
- Budget metric
- Actuals metric
- Variance metric
- Forecast gap metric
- run summary
- report path
- run log path
- human review reminder

## Git Cleanliness Check

After running the app, return to Terminal and run:

```bash
git status
```

Expected result:

```text
nothing to commit, working tree clean
```

The app should generate local reports and run logs only. It should not rewrite tracked workflow JSON during normal runs.

## Why This Matters

The Streamlit interface makes the V1 demo easier to explain to non-technical reviewers.

Instead of asking someone to understand terminal commands first, the demo can show the workflow visually:

```text
choose client
choose export
validate source data
run agent
review output
```

This supports the future Oracle EPM story because it demonstrates how a consultant or finance user could run a controlled reporting workflow from an EPM-style export before any live Oracle API integration exists.

## Important Limits

This demo does not yet:

- connect to Oracle EPM Cloud
- authenticate through OAuth
- call Oracle REST APIs
- write commentary back to EPM
- support production security controls
- replace human finance review

The demo is intentionally local, controlled, and mock-data-based.
