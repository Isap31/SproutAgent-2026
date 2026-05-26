# Design Note: Export-Driven Runs Should Not Dirty Git

When SproutAgent runs from a source export, the preferred V1 behavior is to process the mapped workflow data in memory instead of rewriting the tracked workflow JSON file every time.

## Why

The source export workflow is meant to simulate a future Oracle EPM-style data export. Running the workflow should create local outputs:

```text
report Markdown
run log JSON
```

It should not automatically modify tracked source files unless the user explicitly wants to refresh the baseline workflow JSON.

## Preferred Flow

```text
source_exports/sample_epm_variance_export.csv
↓
validate export
↓
map export to Monthly Board Package data
↓
run SproutAgent from mapped data in memory
↓
generate report and run log
↓
human review
```

## Optional Baseline Refresh

If a user wants to overwrite the tracked workflow JSON, they can use the explicit mapping command with `--write`:

```bash
python3 -m src.map_source_export coruscant-transit-bureau clients/coruscant-transit-bureau/source_exports/sample_epm_variance_export.csv --write
```

This keeps normal demo runs clean while still allowing intentional workflow-source refreshes.
