# SproutAgent Project Status

This file tracks what has been completed, what is currently working, what still needs attention, and what should come next.

## Project Direction

SproutAgent is a mock internal finance execution-agent prototype for the fictional consulting firm **Orbital Horizons Consulting**.

The prototype uses fictional planetary client companies to safely simulate real-world CFO and FP&A consulting workflows, especially finance reporting automation, variance analysis, forecast commentary, finance data support, and executive reporting.

The project is intentionally focused on one company-specific internal consulting workflow rather than a broad public SaaS product.

## Core Positioning

SproutAgent is designed as a controlled execution agent for CFO and FP&A reporting work.

It should help a consulting team turn structured client finance data into draft reporting outputs while preserving validation, traceability, and human review.

Core principle:

```text
Code calculates.
AI narrates.
Humans approve.
```

## Current V1 Workflow

```text
Client folder
↓
Source export or workflow source data
↓
Source validation and mapping, when using exports
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

## Service Focus

SproutAgent is aligned to two mock service lines for Orbital Horizons Consulting.

### 1. Finance Reporting Operations

Focus areas:

- Monthly board package preparation
- Budget vs. actual reporting
- Forecast commentary
- Variance analysis
- Close reporting support
- Executive finance summaries
- Recurring management reporting
- Draft report, PDF, or deck-style outputs

### 2. Finance Data & Decision Support

Focus areas:

- KPI summaries
- Cost driver analysis
- Forecast risk review
- Trend summaries
- Operational finance insights
- Decision-ready executive reporting
- Risk indicators for leadership review

## Current Hero Workflow

**Monthly Board Package**

The current V1 workflow generates a draft CFO/FP&A monthly board package using structured mock finance data.

Outputs include:

- Executive summary
- Budget vs. actual analysis
- Forecast outlook
- KPI summary
- Cost driver explanation
- Risk summary
- Recommended actions
- CFO decision point
- Human review notes
- JSON run log for traceability

## Current Mock CFO Clients

Current mock CFO clients:

- Coruscant Transit Bureau
- Naboo Civic Operations Council
- Hoth Logistics Command
- Endor Eco-Development Authority

Tatooine Water Authority was used as an early test/default client and may be re-added later only if needed.

## Current Client Folder Structure

Client work is organized under one top-level `clients/` folder.

Expected structure:

```text
clients/
├── coruscant-transit-bureau/
│   ├── client_profile.json
│   ├── source_exports/
│   │   └── sample_epm_variance_export.csv
│   ├── workflows/
│   │   └── monthly_board_package.json
│   └── reports/
│       └── monthly_board_package/
│           ├── generated report files
│           └── run_logs/
│
├── naboo-civic-operations-council/
├── hoth-logistics-command/
└── endor-eco-development-authority/
```

## What Has Been Completed So Far

### Repository Setup

- GitHub repository created: `SproutAgent-2026`
- Repository cloned locally to Mac
- `.env.example` added
- `.gitignore` added
- `.env` confirmed ignored by Git
- Generated reports are ignored by Git
- Run logs are ignored by Git
- Local reference notes are ignored where needed
- GitHub project status tracking added

### Mock Consulting Firm Setup

- Mock firm defined as Orbital Horizons Consulting
- Fictional planets are used as mock client companies
- CFO and FP&A teams are the target users
- Project focus narrowed from broad operations consulting to finance execution workflows
- Services reframed around Finance Reporting Operations and Finance Data & Decision Support

### Mock Data Added

- `data/planets.json`
- `data/projects.json`
- `data/risks.json`
- `data/finance_summary.json`
- `data/monthly_board_package.json`

### Client Folder Structure Added

- `clients/coruscant-transit-bureau/client_profile.json`
- `clients/coruscant-transit-bureau/source_exports/README.md`
- `clients/coruscant-transit-bureau/source_exports/sample_epm_variance_export.csv`
- `clients/coruscant-transit-bureau/workflows/monthly_board_package.json`
- `clients/coruscant-transit-bureau/reports/monthly_board_package/.gitkeep`
- `clients/naboo-civic-operations-council/client_profile.json`
- `clients/naboo-civic-operations-council/source_exports/README.md`
- `clients/naboo-civic-operations-council/workflows/monthly_board_package.json`
- `clients/naboo-civic-operations-council/reports/monthly_board_package/.gitkeep`
- `clients/hoth-logistics-command/client_profile.json`
- `clients/hoth-logistics-command/source_exports/README.md`
- `clients/hoth-logistics-command/workflows/monthly_board_package.json`
- `clients/hoth-logistics-command/reports/monthly_board_package/.gitkeep`
- `clients/endor-eco-development-authority/client_profile.json`
- `clients/endor-eco-development-authority/source_exports/README.md`
- `clients/endor-eco-development-authority/workflows/monthly_board_package.json`
- `clients/endor-eco-development-authority/reports/monthly_board_package/.gitkeep`

### Prompt Templates Added

- `prompts/report_prompt.txt`
- `prompts/risk_prompt.txt`
- `prompts/timeline_prompt.txt`
- `prompts/cfo_brief_prompt.txt`

### Documentation Added

- `README.md`
- `docs/roadmap.md`
- `docs/architecture.md`
- `docs/project_status.md`
- `docs/v1_demo_checklist.md`
- `docs/service_focus.md`
- `docs/oracle_epm_integration_plan.md`
- `docs/source_export_workflow.md`
- `AGENTS.md`

### Python Modules Added

- `src/__init__.py`
- `src/intake.py`
- `src/prompt_builder.py`
- `src/gemini_service.py`
- `src/report_generator.py`
- `src/orchestrator.py`
- `src/agent.py`
- `src/client_registry.py`
- `src/main.py`
- `src/run_all_clients.py`
- `src/validate_source_export.py`
- `src/map_source_export.py`
- `src/run_source_export_workflow.py`

### Skills Package Added

- `src/skills/__init__.py`
- `src/skills/data_pull.py`
- `src/skills/validation.py`
- `src/skills/metric_calculation.py`
- `src/skills/narrative_generation.py`
- `src/skills/output_generation.py`
- `src/skills/run_logging.py`
- `src/skills/source_export_validation.py`
- `src/skills/source_mapping.py`

### Agent Control Layer Completed

- `src/agent.py` wraps the orchestrator in a controlled SproutAgent run layer
- Agent run summary is printed in the terminal
- Agent tracks selected client folder
- Agent tracks selected workflow
- Agent tracks AI mode
- Agent tracks execution steps
- Agent tracks output path
- Agent marks human review as required
- Agent saves a JSON run log for traceability

### Client Discovery Added

- `src/client_registry.py` lists available client folders
- If no `SPROUT_CLIENT_FOLDER` is selected, SproutAgent shows available clients and stops safely
- The previous confusing shared-data fallback behavior has been removed from the normal run path
- SproutAgent now expects a client folder to be selected before generating a report

### Output Behavior Completed

- Markdown reports save under the selected client's `reports/monthly_board_package/` folder
- JSON run logs save under the selected client's `reports/monthly_board_package/run_logs/` folder
- Terminal output prints the selected client, workflow, AI mode, report output path, run log path, execution steps, metric summary, and human review reminder
- Terminal output gives a helpful next-step command to open the selected client's report folder

### V1 Smoke Test Added

- `src/run_all_clients.py` runs the Monthly Board Package workflow for every active client folder
- Smoke test confirmed 4 active client workflows passed successfully
- Smoke test validates that reports and run logs generate across all active mock clients

### Source Export Workflow Added

- Coruscant now includes a mock Oracle EPM-style source export: `sample_epm_variance_export.csv`
- `src/skills/source_export_validation.py` validates required export columns and numeric fields
- `src/validate_source_export.py` provides a CLI command to validate the export
- `src/skills/source_mapping.py` maps an Oracle EPM-style CSV export into Monthly Board Package workflow data
- `src/map_source_export.py` previews mapped workflow JSON and can write it to `workflows/monthly_board_package.json` using `--write`
- `src/run_source_export_workflow.py` runs the full source-export-to-report flow in one command
- `docs/source_export_workflow.md` documents the validation, mapping, write, and report-generation flow

### Working Local Capabilities

- Local terminal workflow runs
- Monthly Board Package workflow runs
- Client-folder data loading works
- Source export validation works
- Source export mapping works
- Source export can refresh the Coruscant workflow JSON
- Full source-export-to-report command exists
- Required data fields validate successfully
- Budget, actuals, variance, forecast, and forecast gap metrics calculate successfully
- Markdown report generates successfully
- JSON run log generates successfully
- Human review header appears in report output
- Offline fallback mode works
- Generated reports and run logs remain local outputs

### Gemini Work Completed

- `.env` loading issue fixed
- Gemini API key visibility tested safely
- Exposed API key was replaced by user
- Old `google-generativeai` SDK was identified as deprecated
- Local environment upgraded to `google-genai`
- Model was updated locally from `gemini-1.5-flash` to `gemini-2.0-flash`
- Live Gemini call now reaches Google API
- Current Gemini blocker is quota exhaustion, not project code failure

## Source Data Direction

Current V1 source data can come from:

1. Prepared client workflow JSON
2. Mock Oracle EPM-style CSV export mapped into workflow JSON

Future source data direction:

```text
Mock JSON data
↓
Oracle EPM-style CSV export
↓
CSV / Excel exports
↓
NetSuite or QuickBooks exports
↓
Approved API connectors
```

SproutAgent should not replace Oracle EPM, NetSuite, or QuickBooks. Those systems would remain the source of record. SproutAgent would act as a reporting execution layer after approved data is exported or pulled.

## Oracle EPM Direction

SproutAgent is now being shaped toward an Oracle EPM-style future demo.

Current Oracle EPM-aware path:

```text
Oracle EPM-style export
↓
Validate export
↓
Map export into Monthly Board Package workflow data
↓
Run SproutAgent
↓
Generate report and run log
↓
Human review
```

This keeps V1 grounded while preparing for future Oracle EPM access, REST APIs, AI Agent Studio concepts, or embedded workflow patterns.

## Real Demo Growth Options

The project should grow in this order after V1 is stable:

### Option 2: Streamlit or Local Demo Interface

Create a simple local interface where a user can select a client, choose a workflow, run SproutAgent, and open the generated report.

### Option 3: Excel / CSV Intake

Expand the `source_exports/` approach so SproutAgent can convert more CSV or Excel exports into workflow-ready source data.

### Option 4: Internal Company Workflow Interface

Build a more polished internal workflow interface for consultants to run approved workflows without using terminal commands.

### Option 5: Model Provider Layer

Add a provider layer so SproutAgent can support Gemini now and Claude later without rewriting the workflow logic.

## Current Known Issues

- Live Gemini calls may fail because the current Gemini quota is exhausted
- Offline fallback mode is useful for development but should not be the main long-term workflow
- Requirements file may need to be confirmed/updated to match `google-genai`
- Some GitHub write actions have occasionally been blocked and may require manual updates
- V1 should be hardened before adding Skill 002
- Generated reports and run logs are local outputs and should not be committed as project source files
- The source export mapping currently exists for a Coruscant sample CSV only

## Current Recommended Commands

Run discovery/safe-stop mode:

```bash
SPROUT_OFFLINE_MODE=true python3 -m src.main
```

Run the stable local development workflow for Coruscant:

```bash
SPROUT_CLIENT_FOLDER=coruscant-transit-bureau SPROUT_OFFLINE_MODE=true python3 -m src.main
```

Run every active client folder as a V1 smoke test:

```bash
python3 -m src.run_all_clients
```

Validate the default sample source export:

```bash
python3 -m src.validate_source_export
```

Preview mapped Monthly Board Package data from the source export:

```bash
python3 -m src.map_source_export
```

Write mapped source export data into the Coruscant workflow file:

```bash
python3 -m src.map_source_export coruscant-transit-bureau clients/coruscant-transit-bureau/source_exports/sample_epm_variance_export.csv --write
```

Run the full source-export-to-report workflow:

```bash
python3 -m src.run_source_export_workflow
```

Run live Gemini mode when quota is available:

```bash
SPROUT_CLIENT_FOLDER=coruscant-transit-bureau python3 -m src.main
```

Open generated reports for Coruscant:

```bash
open clients/coruscant-transit-bureau/reports/monthly_board_package
```

Check Git status:

```bash
git status
```

## Product Principles To Preserve

- Mock firm, real workflow
- Fake data, serious business problem
- Code calculates
- AI narrates
- Humans approve
- Terminal first, integrations later
- Do not overbuild before V1 is stable
- Generated reports should not be committed
- API keys should never be committed
- SproutAgent is a controlled internal workflow prototype, not a broad autonomous agent
- Oracle EPM readiness should be built through exports and mapping before live APIs

## Future Ideas Parking Lot

These ideas should remain parked until V1 is clean and stable:

- Close Reporting skill
- SaaS KPI Review skill
- PowerPoint output
- Claude provider support
- Model comparison mode
- Excel add-in
- Planning system integration
- AI commentary inside finance workflows
- Oracle EPM REST API integration
- NetSuite / QuickBooks live API integrations

## Next Best Steps

1. Pull latest GitHub updates locally
2. Test `python3 -m src.run_source_export_workflow`
3. Confirm the refreshed workflow file still runs through SproutAgent
4. Confirm reports and run logs are generated in the correct Coruscant folder
5. Confirm generated reports/run logs do not appear in `git status`
6. Polish the Monthly Board Package report quality further if needed
7. Then consider a small Streamlit/local demo interface after the export-driven flow is stable

## V1 Definition of Done

V1 is demo-ready when:

1. A selected client folder can be run from terminal.
2. The workflow completes without manual code edits.
3. The report is saved under the selected client's report folder.
4. The run log is saved under the selected client's report folder.
5. The terminal clearly explains what happened.
6. The terminal gives the correct command to open the selected client's report folder.
7. The report is clearly marked as a draft for human review.
8. Generated outputs are not committed to GitHub.
9. The project can be explained in under three minutes.
10. The Coruscant source export can be validated, mapped, and used to generate a report.

## Last Updated

2026-05-25
