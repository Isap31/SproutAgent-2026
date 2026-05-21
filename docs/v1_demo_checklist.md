# SproutAgent V1 Demo Checklist

This checklist keeps the V1 demo focused and prevents the project from drifting into future features too early.

## V1 Demo Goal

SproutAgent should demonstrate a controlled CFO/FP&A execution-agent workflow that turns structured client finance data into a draft Monthly Board Package for human review.

## Core Demo Flow

```text
Client folder
↓
Workflow source data
↓
SproutAgent control layer
↓
Data pull
↓
Validation
↓
Metric calculation
↓
Narrative generation
↓
Markdown report output
↓
Run log output
↓
Human review
```

## V1 Must-Haves

- [x] One top-level `clients/` folder
- [x] Client folders for mock CFO clients
- [x] `client_profile.json` for each client
- [x] `workflows/monthly_board_package.json` for each client
- [x] `reports/monthly_board_package/` for each client
- [x] SproutAgent control layer
- [x] Execution step tracking
- [x] Run summary in terminal
- [x] Markdown report output
- [x] JSON run log output
- [x] Human review required in terminal and report output
- [x] Generated reports ignored by Git
- [x] Run logs ignored by Git

## Current Demo Command

Use offline mode for reliable local demos while Gemini quota is unavailable:

```bash
SPROUT_CLIENT_FOLDER=coruscant-transit-bureau SPROUT_OFFLINE_MODE=true python3 -m src.main
```

## What The Demo Should Show

The terminal should show:

- selected client
- selected workflow
- AI mode
- output report path
- run log path
- execution steps
- metric summary
- human review reminder

## What The Report Should Show

The generated Markdown report should include:

- SproutAgent traceability header
- client name
- client folder
- reporting period
- AI mode
- source data context
- executive summary
- budget vs. actuals
- forecast outlook
- KPI summary
- cost drivers
- risks
- recommended actions
- CFO decision point
- human review notes

## What The Run Log Should Show

The generated JSON run log should include:

- agent name
- workflow
- client name
- client folder
- AI mode
- run status
- timestamps
- output path
- calculated metrics
- execution steps
- human review requirement

## Do Not Add Yet

These are intentionally parked until V1 is stable:

- Skill 002: Close Reporting
- SaaS KPI Review
- Excel or CSV intake
- PowerPoint output
- Claude provider support
- model comparison
- Excel add-in
- planning system integration
- real client data connectors

## V1 Definition of Done

V1 is demo-ready when:

1. A selected client folder can be run from terminal.
2. The workflow completes without manual code edits.
3. The report is saved under the selected client's report folder.
4. The run log is saved under the selected client's report folder.
5. The terminal clearly explains what happened.
6. The report is clearly marked as a draft for human review.
7. Generated outputs are not committed to GitHub.
