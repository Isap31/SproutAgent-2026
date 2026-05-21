# SproutAgent 2026

SproutAgent is a mock CFO and FP&A execution-agent prototype for a fictional consulting firm called **Orbital Horizons Consulting**.

The project uses fictional planetary client companies to safely simulate real-world finance transformation, reporting automation, operational risk, variance analysis, and executive decision-support workflows.

This is not a true autonomous agent. Phase 1 is intentionally designed as a controlled **Execution Agent**: one orchestrator, reusable deterministic finance skills, standardized outputs, and human review.

## Project Purpose

SproutAgent is being built to explore how AI can help consulting and finance teams reduce repetitive reporting work while keeping humans in control.

The prototype focuses on CFO and FP&A use cases such as:

- Monthly board packages
- Budget vs. actual variance analysis
- Forecast commentary
- Cost driver analysis
- KPI summaries
- Close reporting support
- Executive finance narratives
- Human-reviewed reporting outputs

## Core Concept

Orbital Horizons Consulting treats fictional planets as client companies. Each client has finance, operational, risk, and transformation problems.

SproutAgent uses mock data to simulate a real consulting workflow:

```text
Client Data Sources
↓
Data Pull Skill
↓
Validation Skill
↓
Metric Calculation Skill
↓
Narrative Generation Skill
↓
Deck / PDF / Markdown Output Skill
↓
Human Review
```

## Phase 1: Execution Agent

Phase 1 is focused on building a practical execution workflow, not a fully autonomous AI agent.

The system should:

1. Pull structured mock finance data
2. Validate required fields
3. Calculate finance and KPI metrics deterministically
4. Use Gemini for narrative generation
5. Produce standardized reporting outputs
6. Route outputs to human review

This creates most of the practical value while keeping the workflow understandable, auditable, and safe.

## V1 Hero Skill: Monthly Board Package

The first reusable finance skill is the **Monthly Board Package**.

### Inputs

- Mock client profile
- Reporting month
- Budget
- Actuals
- Forecast
- Prior month actuals
- KPI data
- Cost drivers
- Leadership notes
- Risk indicators

### Outputs

- KPI summary
- Budget vs. actual variance analysis
- Forecast commentary
- Executive finance narrative
- Cost driver explanation
- Risk summary
- CFO decision point
- Draft report for human review

## Future Finance Skills

SproutAgent is designed to support a reusable skills library.

### Skill: SaaS KPI Review

Potential outputs:

- ARR bridge
- Burn multiple analysis
- CAC / LTV commentary
- Hiring efficiency analysis
- Anomaly flags
- CFO recommendation summary

### Skill: Close Reporting

Potential outputs:

- Automated close package
- Journal review summaries
- Flux commentary
- Cash analysis
- Open item summary
- Human review checklist

## Current Mock Clients

- Tatooine Water Authority — resource distribution, cost pressure, and supply chain modernization
- Coruscant Transit Bureau — infrastructure congestion, budget overruns, and operating efficiency
- Naboo Civic Operations Council — public-sector digital transformation and service reporting
- Hoth Logistics Command — remote logistics, weather disruption, and forecast volatility
- Endor Eco-Development Authority — sustainability investment and financial constraint management

## Current Repository Structure

```text
SproutAgent-2026/
├── data/
│   ├── monthly_board_package.json
│   ├── planets.json
│   ├── projects.json
│   ├── risks.json
│   └── finance_summary.json
├── docs/
│   ├── architecture.md
│   └── roadmap.md
├── prompts/
│   ├── cfo_brief_prompt.txt
│   ├── report_prompt.txt
│   ├── risk_prompt.txt
│   └── timeline_prompt.txt
├── src/
│   ├── __init__.py
│   ├── gemini_service.py
│   ├── intake.py
│   ├── prompt_builder.py
│   ├── report_generator.py
│   └── skills/
│       ├── __init__.py
│       ├── data_pull.py
│       └── validation.py
├── .env.example
└── README.md
```

## Current Build Status

Completed so far:

- Project README updated for the consulting prototype
- Mock planetary client data added
- Mock project data added
- Risk taxonomy added
- CFO briefing prompt added
- General consulting, risk, and timeline prompts added
- Architecture and roadmap documentation added
- Gemini service scaffold added
- Prompt builder added
- Report generator added
- Monthly board package mock data added
- Skills package started
- Data pull skill added
- Validation skill added

Still needed:

- Metric calculation skill
- Narrative generation skill
- Output generation skill
- Orchestrator
- Main runner script
- Requirements file
- First generated sample report

## Planned Architecture

```text
User selects skill
↓
SproutAgent Orchestrator
↓
Data Pull Skill
↓
Validation Skill
↓
Metric Calculation Skill
↓
Narrative Generation Skill using Gemini
↓
Output Generation Skill
↓
Human Review
```

## Gemini and Future Model Flexibility

The first version is being built around Gemini as the narrative generation engine.

Future versions may add a model-provider layer so SproutAgent can support other approved models without rebuilding the workflow.

The long-term goal is not to tie the product to one model. The goal is to build reusable finance workflows where the AI model is one interchangeable part of the system.

## Quick Start

This project is still under construction.

Eventually, the local workflow will be:

```bash
pip install -r requirements.txt
python src/main.py
```

For now, the repo contains the planning docs, mock data, prompt templates, and early execution-agent modules.

## Human Review Principle

SproutAgent is a copilot and execution assistant. It is not a final decision-maker.

All AI-generated finance narratives, reporting outputs, and recommendations should be reviewed, edited, and approved by a human consultant or finance professional before use.

## Long-Term Vision

SproutAgent begins as a mock consulting simulation, but the long-term vision is a realistic finance execution prototype that helps CFO and FP&A teams automate repeatable reporting workflows, standardize outputs, and turn structured data into decision-ready narratives.

## Contact

**Caitlin Przywara**  
GitHub: @Isap31
