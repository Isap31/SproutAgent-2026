# SproutAgent Project Status

This file tracks what has been completed, what is currently working, what still needs attention, and what should come next.

## Project Direction

SproutAgent is a mock CFO and FP&A execution-agent prototype for a fictional consulting firm called Orbital Horizons Consulting.

The prototype uses fictional planetary client companies to safely simulate real-world finance transformation, reporting automation, operational risk, variance analysis, and executive decision-support workflows.

The current goal is to harden V1 before adding additional skills or integrations.

## Current V1 Workflow

```text
Mock CFO/FP&A data
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
Human review
```

## Current Hero Workflow

**Monthly Board Package**

Current mock client:

**Tatooine Water Authority**

This workflow generates a draft CFO/FP&A monthly board package using mock finance data.

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

### Prompt Templates Added

- `prompts/report_prompt.txt`
- `prompts/risk_prompt.txt`
- `prompts/timeline_prompt.txt`
- `prompts/cfo_brief_prompt.txt`

### Documentation Added

- `README.md`
- `docs/roadmap.md`
- `docs/architecture.md`
- `AGENTS.md`

### Python Modules Added

- `src/__init__.py`
- `src/intake.py`
- `src/prompt_builder.py`
- `src/gemini_service.py`
- `src/report_generator.py`
- `src/orchestrator.py`
- `src/main.py`

### Skills Package Added

- `src/skills/__init__.py`
- `src/skills/data_pull.py`
- `src/skills/validation.py`
- `src/skills/metric_calculation.py`
- `src/skills/narrative_generation.py`
- `src/skills/output_generation.py`

### Working Local Capabilities

- Local terminal workflow runs
- Monthly Board Package workflow runs
- Mock board package data loads successfully
- Required data fields validate successfully
- Budget, actuals, variance, forecast, and forecast gap metrics calculate successfully
- Markdown report generates successfully
- Report saves to `reports/`
- Human review header appears in report output
- Offline fallback mode works
- Terminal output now shows workflow summary and key metrics

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

## Current Recommended Commands

Run the stable local development workflow:

```bash
SPROUT_OFFLINE_MODE=true python3 -m src.main
```

Run live Gemini mode when quota is available:

```bash
python3 -m src.main
```

Open generated reports:

```bash
open reports
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
2. Keep Monthly Board Package workflow stable
3. Confirm report header and source-data context look clean
4. Add a short demo guide if needed
5. Avoid adding Skill 002 until V1 is polished

## Last Updated

2026-05-21
