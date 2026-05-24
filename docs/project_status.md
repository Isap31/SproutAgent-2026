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

- Tatooine Water Authority
- Coruscant Transit Bureau
- Naboo Civic Operations Council
- Hoth Logistics Command
- Endor Eco-Development Authority

## Current Client Folder Structure

Client work is organized under one top-level `clients/` folder.

Expected structure:

```text
clients/
├── coruscant-transit-bureau/
│   ├── client_profile.json
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
- `clients/coruscant-transit-bureau/workflows/monthly_board_package.json`
- `clients/coruscant-transit-bureau/reports/monthly_board_package/.gitkeep`
- `clients/naboo-civic-operations-council/client_profile.json`
- `clients/naboo-civic-operations-council/workflows/monthly_board_package.json`
- `clients/naboo-civic-operations-council/reports/monthly_board_package/.gitkeep`
- `clients/hoth-logistics-command/client_profile.json`
- `clients/hoth-logistics-command/workflows/monthly_board_package.json`
- `clients/hoth-logistics-command/reports/monthly_board_package/.gitkeep`
- `clients/endor-eco-development-authority/client_profile.json`
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

### Skills Package Added

- `src/skills/__init__.py`
- `src/skills/data_pull.py`
- `src/skills/validation.py`
- `src/skills/metric_calculation.py`
- `src/skills/narrative_generation.py`
- `src/skills/output_generation.py`
- `src/skills/run_logging.py`

### Agent Control Layer Completed

- `src/agent.py` now wraps the orchestrator in a controlled SproutAgent run layer
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
- Terminal output now prints the selected client, workflow, AI mode, report output path, run log path, execution steps, metric summary, and human review reminder
- Terminal output now gives a helpful next-step command to open the selected client's report folder

### Working Local Capabilities

- Local terminal workflow runs
- Monthly Board Package workflow runs
- Client-folder data loading works
- Example tested successfully with `coruscant-transit-bureau`
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

Current V1 source data is mock JSON under client folders.

Future source data direction:

```text
Mock JSON data
↓
CSV / Excel exports
↓
NetSuite or QuickBooks exports
↓
Approved API connectors
```

SproutAgent should not replace NetSuite or QuickBooks. Those systems would remain the source of record. SproutAgent would act as a reporting execution layer after approved data is exported or pulled.

## Real Demo Growth Options

The project should grow in this order after V1 is stable:

### Option 2: Streamlit or Local Demo Interface

Create a simple local interface where a user can select a client, choose a workflow, run SproutAgent, and open the generated report.

### Option 3: Excel / CSV Intake

Add a `source_exports/` folder to each client and allow SproutAgent to convert CSV or Excel exports into workflow-ready source data.

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

## Current Recommended Commands

Run discovery/safe-stop mode:

```bash
SPROUT_OFFLINE_MODE=true python3 -m src.main
```

Run the stable local development workflow for Coruscant:

```bash
SPROUT_CLIENT_FOLDER=coruscant-transit-bureau SPROUT_OFFLINE_MODE=true python3 -m src.main
```

Run another client folder:

```bash
SPROUT_CLIENT_FOLDER=hoth-logistics-command SPROUT_OFFLINE_MODE=true python3 -m src.main
```

Run live Gemini mode when quota is available:

```bash
SPROUT_CLIENT_FOLDER=coruscant-transit-bureau python3 -m src.main
```

Open generated reports for a selected client:

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
- NetSuite / QuickBooks live API integrations

## Next Best Steps

1. Pull latest GitHub updates locally
2. Test the new terminal next-step output
3. Test every client folder with offline mode
4. Confirm all client runs save reports and run logs correctly
5. Polish the Monthly Board Package report quality
6. Update documentation after each meaningful milestone
7. Then consider CSV/Excel intake as the next bridge toward real data

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

## Last Updated

2026-05-23
