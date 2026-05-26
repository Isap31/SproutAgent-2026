# Milestone: Clean Source-Export Runs

## Status

Completed.

## What Changed

SproutAgent can now run the Oracle EPM-style source export workflow without rewriting tracked workflow JSON files by default.

Preferred flow:

```text
source_exports/sample_epm_variance_export.csv
↓
validate export
↓
map export into Monthly Board Package data in memory
↓
run SproutAgent from mapped data
↓
generate Markdown report
↓
generate JSON run log
↓
human review
```

## Why This Matters

Earlier source-export runs refreshed `clients/coruscant-transit-bureau/workflows/monthly_board_package.json`, which made Git show tracked file changes after every demo run.

The new behavior keeps the normal demo workflow clean:

```text
python3 -m src.run_source_export_workflow
↓
git status
↓
nothing to commit, working tree clean
```

## Current Hero Command

```bash
python3 -m src.run_source_export_workflow
```

## What This Proves

SproutAgent now has a cleaner Oracle EPM-style demo path:

```text
mock EPM-style export
→ validation
→ in-memory mapping
→ controlled agent run
→ report + run log
→ human review
```

This supports the longer-term goal of building toward Oracle EPM, CSV, Excel, or other approved finance-system exports without making the repo messy during normal demo runs.

## Optional Baseline Refresh

The tracked workflow JSON can still be intentionally refreshed with:

```bash
python3 -m src.map_source_export coruscant-transit-bureau clients/coruscant-transit-bureau/source_exports/sample_epm_variance_export.csv --write
```

That command should be used only when the project intentionally wants to update the saved workflow source.
