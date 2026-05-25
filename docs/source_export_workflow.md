# Source Export Workflow

This guide explains the current Oracle EPM-style source export workflow for SproutAgent.

## Purpose

SproutAgent V1 still runs from client workflow JSON files. The source export workflow is the bridge toward future Oracle EPM, CSV, or Excel intake.

The current source export path is:

```text
Oracle EPM-style CSV export
↓
Validate export columns and numeric fields
↓
Map export into Monthly Board Package workflow data
↓
Write mapped data to workflows/monthly_board_package.json
↓
Run SproutAgent
↓
Generate report and run log
↓
Human review
```

## Current Sample Export

The current sample export lives here:

```text
clients/coruscant-transit-bureau/source_exports/sample_epm_variance_export.csv
```

This file is a mock Oracle EPM-style variance export. It is not real client data.

## Required Columns

The current validation skill expects these columns:

```text
account
entity
scenario
period
budget
actuals
forecast
prior_month_actuals
kpi_name
kpi_value
cost_driver
risk_indicator
leadership_note
```

## Validate the Source Export

Run:

```bash
python3 -m src.validate_source_export
```

Or validate a specific file:

```bash
python3 -m src.validate_source_export clients/coruscant-transit-bureau/source_exports/sample_epm_variance_export.csv
```

Expected successful output:

```text
Source Export Validation
Status: PASSED
Rows checked: 4
Ready for mapping: True
```

## Preview the Mapped Workflow Data

Run:

```bash
python3 -m src.map_source_export
```

This prints the mapped Monthly Board Package JSON to the terminal without overwriting the client workflow file.

## Write the Mapped Data to the Client Workflow

Run:

```bash
python3 -m src.map_source_export coruscant-transit-bureau clients/coruscant-transit-bureau/source_exports/sample_epm_variance_export.csv --write
```

This updates:

```text
clients/coruscant-transit-bureau/workflows/monthly_board_package.json
```

## Run SproutAgent From the Updated Workflow

After writing the mapped data, run:

```bash
SPROUT_CLIENT_FOLDER=coruscant-transit-bureau SPROUT_OFFLINE_MODE=true python3 -m src.main
```

SproutAgent will then generate:

```text
clients/coruscant-transit-bureau/reports/monthly_board_package/<report>.md
clients/coruscant-transit-bureau/reports/monthly_board_package/run_logs/<run-log>.json
```

## Open the Report Folder

Run:

```bash
open clients/coruscant-transit-bureau/reports/monthly_board_package
```

## Important Data Safety Note

Do not commit sensitive or real client financial data to GitHub.

For now, only mock exports should live in the repository. Real Oracle EPM, NetSuite, QuickBooks, or client finance exports should remain local, sanitized, or stored only in an approved secure environment.

## Why This Matters

This workflow proves the next major bridge in SproutAgent:

```text
Mock prepared workflow JSON
↓
Export-driven workflow JSON
↓
Future CSV / Excel intake
↓
Future Oracle EPM integration
```

This keeps V1 focused while making the agent architecture ready for real finance-system data later.
