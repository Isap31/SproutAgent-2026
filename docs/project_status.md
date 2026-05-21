# SproutAgent Project Status

This file tracks what has been completed, what is currently working, what still needs attention, and what should come next.

## Project Direction

SproutAgent is a mock CFO and FP&A execution-agent prototype for a fictional consulting firm called Orbital Horizons Consulting.

The prototype uses fictional planetary client companies to safely simulate real-world finance transformation, reporting automation, operational risk, variance analysis, and executive decision-support workflows.

The current goal is to harden V1 before adding additional skills or integrations.

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

## Current Hero Workflow

**Monthly Board Package**

The current V1 workflow generates a draft CFO/FP&A monthly board package using structured mock finance data.

Current mock CFO clients:

- Tatooine Water Authority
- Coruscant Transit Bureau
- Naboo Civic Operations Council
- Hoth Logistics Command
- Endor Eco-Development Authority

## Current Client Folder Structure

Client work is now organized under a single top-level `clients/` folder.

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
- Local Gemini API key setup tested
- Generated reports folder used locally
- Generated reports are ignored by Git

### Mock Consulting Firm Setup

- Mock firm defined as Orbital Horizons Consulting
- Fictional planets are used as mock client companies
- CFO and FP&A teams are the target clientele
- The project focus was narrowed from general operations consulting to finance execution workflows

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
- `AGENTS.md`

### Python Modules Added

- `src/__init__.py`
- `src/intake.py`
- `src/prompt_builder.py`
- `src/gemini_service.py`
- `src/report_generator.py`
- `src/orchestrator.py`
- `src/agent.py`
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

### Working Local Capabilities

- Local terminal workflow runs
- Monthly Board Package workflow runs
- Client-folder data loading works
- Example tested successfully with `coruscant-transit-bureau`
- Required data fields validate successfully
- Budget, actuals, variance, forecast, and forecast gap metrics calculate successfully
- Markdown report generates successfully
- Report saves under the selected client's `reports/monthly_board_package/` folder
- Run log saves under the selected client's `reports/monthly_board_package/run_logs/` folder
- Human review header appears in report output
- Offline fallback mode works
- Terminal output now shows workflow summary, execution steps, output path, run log path, and key metrics

### Gemini Work Completed

- `.env` loading issue fixed
- Gemini API key visibility tested safely
- Exposed API key was replaced by user
- Old `google-generativeai` SDK was identified as deprecated
- Local environment upgraded to `google-genai`
- Model was updated locally from `gemini-1.5-flash` to `gemini-2.0-flash`
- Live Gemini call now reaches Google API
- Current Gemini blocker is quota exhaustion, not project code failure

## Current Known Issues

- Live Gemini calls may fail because the current Gemini quota is exhausted
- Offline fallback mode is useful for development but should not be the main long-term workflow
- Requirements file may need to be confirmed/updated to match `google-genai`
- Some GitHub write actions have occasionally been blocked and may require manual updates
- V1 should be hardened before adding Skill 002
- Generated reports and run logs are local outputs and should not be committed as project source files

## Current Recommended Commands

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

## Future Ideas Parking Lot

These ideas should remain parked until V1 is clean and stable:

- Close Reporting skill
- SaaS KPI Review skill
- Excel or CSV input
- PowerPoint output
- Claude provider support
- Model comparison mode
- Excel add-in
- Planning system integration
- AI commentary inside finance workflows

## Next Best Steps

1. Confirm `requirements.txt` uses the correct Gemini SDK package
2. Confirm all client folders follow the same structure
3. Keep Monthly Board Package workflow stable
4. Confirm report header and source-data context look clean
5. Confirm run logs should remain local outputs and not source-controlled artifacts
6. Avoid adding Skill 002 until V1 is polished

## Last Updated

2026-05-21
