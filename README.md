# SproutAgent 2026

SproutAgent is a mock CFO and FP&A execution-agent prototype for the fictional consulting firm **Orbital Horizons Consulting**.

The project uses fictional client companies and mock finance data to safely simulate real-world finance reporting automation, variance analysis, forecast commentary, and executive decision-support workflows.

SproutAgent is not a fully autonomous agent and it is not a replacement for Oracle EPM, NetSuite, QuickBooks, CFOs, FP&A analysts, or consultants. It is a controlled execution assistant that validates source data, calculates finance metrics deterministically, generates draft reporting narratives, saves outputs, and keeps human review visible.

## Core Principle

```text
Code calculates.
AI narrates.
Humans approve.
```

## Current Hero Workflow

The current V1 workflow is the **Monthly Board Package**.

It supports:

- Budget vs. actual variance analysis
- Forecast gap analysis
- KPI commentary
- Cost driver summaries
- Risk and leadership notes
- CFO decision points
- Markdown report generation
- JSON run logging
- Human review reminders

## Current Demo Story

SproutAgent now has a clean Oracle EPM-style demo path:

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

The source-export workflow runs in memory during normal demos, so it does **not** rewrite tracked workflow JSON files or dirty Git by default.

## Current Mock Clients

Current mock client display names include:

- Coruscant Transit Authority
- Naboo Public Works
- Endor Infrastructure
- Hoth Logistics Command, if present locally

Internal folder slugs may still use longer stable names such as:

```text
clients/coruscant-transit-bureau/
clients/naboo-civic-operations-council/
clients/endor-eco-development-authority/
```

This is intentional. The folder slugs are stable internal IDs, while `client_name` values are friendly display names.

## Run the Terminal Demo

From the project root, run the source-export workflow:

```bash
python3 -m src.run_source_export_workflow
```

Then confirm Git stayed clean:

```bash
git status
```

Expected result:

```text
nothing to commit, working tree clean
```

## Run the Local Streamlit Demo

Install Streamlit locally if needed:

```bash
pip3 install streamlit
```

Launch the app from the project root:

```bash
streamlit run src/demo_app.py
```

The app allows you to:

- Select a client by friendly display name
- Select a source export CSV
- Validate the export
- Run SproutAgent from mapped in-memory data
- View key metrics
- View the run summary
- Open the generated report folder

## Important Data Safety Note

Do not commit sensitive or real client financial data to GitHub.

For now, only mock exports and mock workflow files should live in the repository. Real Oracle EPM, NetSuite, QuickBooks, or client finance exports should remain local, sanitized, or stored only in an approved secure environment.

## Current Repository Structure

```text
SproutAgent-2026/
├── clients/
│   └── <client-folder>/
│       ├── client_profile.json
│       ├── source_exports/
│       ├── workflows/
│       └── reports/
├── docs/
├── prompts/
├── src/
│   ├── agent.py
│   ├── demo_app.py
│   ├── main.py
│   ├── run_source_export_workflow.py
│   └── skills/
├── .env.example
├── requirements.txt
└── README.md
```

## Key Documentation

- `docs/project_status.md` — full project status tracker
- `docs/source_export_workflow.md` — source export validation/mapping guide
- `docs/local_demo_interface.md` — Streamlit demo guide
- `docs/oracle_epm_integration_plan.md` — future Oracle EPM direction
- `docs/milestone_clean_source_export_runs.md` — clean in-memory export run milestone

## Gemini and Future Model Flexibility

The first version uses Gemini for narrative generation when quota is available. Offline fallback mode is available for local development and demo stability.

Future versions may add a provider layer so SproutAgent can support other approved models, such as Claude, without rewriting the workflow logic.

## Human Review Principle

SproutAgent is a copilot and execution assistant. It is not a final decision-maker.

All AI-generated finance narratives, reporting outputs, and recommendations should be reviewed, edited, and approved by a human consultant or finance professional before use.

## Long-Term Vision

SproutAgent begins as a mock consulting simulation, but the long-term vision is a realistic finance execution prototype that helps CFO and FP&A teams automate repeatable reporting workflows, standardize outputs, and turn structured finance-system data into decision-ready narratives.

## Contact

**Caitlin Przywara**  
GitHub: @Isap31
