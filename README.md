# SproutAgent 2026

SproutAgent is a mock CFO and FP&A execution-agent prototype for a fictional consulting firm called **Orbital Horizons Consulting**.

The project uses fictional planetary client companies to safely simulate real-world finance transformation, reporting automation, operational risk, variance analysis, and executive decision-support workflows.

SproutAgent is not designed as a fully autonomous agent. It is a controlled execution assistant: it runs reusable finance skills, calculates metrics deterministically, generates draft narratives with AI, and routes outputs to human review.

## Why This Project Exists

Finance teams often spend significant time assembling recurring reports, explaining variances, preparing leadership updates, and translating financial data into executive-ready narratives.

SproutAgent explores how AI can reduce that manual reporting burden while keeping finance professionals and consultants in control of the final output.

The prototype focuses on CFO and FP&A needs such as:

- Monthly board reporting
- Budget vs. actual variance analysis
- Forecast commentary
- Cost driver analysis
- KPI summaries
- Close reporting support
- Executive finance narratives
- Human-reviewed reporting outputs

## Core Operating Model

Orbital Horizons Consulting treats fictional planets as client companies. Each mock client has finance, operational, risk, and transformation challenges.

SproutAgent follows a controlled finance workflow:

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

The most important design rule is:

```text
Code calculates.
AI narrates.
Humans approve.
```

This keeps the workflow practical, auditable, and finance-friendly.

## Most Important Product Factors

### 1. Deterministic Finance Logic

Financial calculations should be handled by code, not guessed by the AI model.

Examples:

- Variance amount
- Variance percentage
- Forecast gap
- Month-over-month change
- KPI movement
- Cost driver summaries

### 2. AI-Assisted Narrative Generation

Gemini is used to draft executive-ready commentary after the numbers are calculated.

Example outputs:

- CFO summaries
- Variance explanations
- Forecast commentary
- Risk narratives
- Recommended actions
- Decision points

### 3. Standardized Outputs

SproutAgent should produce consistent report structures so finance teams do not rebuild the same deliverables from scratch every month.

### 4. Human Review

Every output is treated as a draft. A consultant, CFO, or FP&A professional must review the final narrative before it is used.

### 5. Reusable Finance Skills

SproutAgent is built around reusable skills instead of one vague chatbot experience.

Each skill should define:

- Required inputs
- Validation rules
- Calculated metrics
- AI narrative tasks
- Final output format
- Human review checklist

## Current Hero Workflow: Monthly Board Package

The first major workflow is the **Monthly Board Package**.

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
│   ├── main.py
│   ├── orchestrator.py
│   ├── prompt_builder.py
│   ├── report_generator.py
│   └── skills/
│       ├── __init__.py
│       ├── data_pull.py
│       ├── metric_calculation.py
│       ├── narrative_generation.py
│       ├── output_generation.py
│       └── validation.py
├── .env.example
└── README.md
```

## Gemini and Future Model Flexibility

The first version is being built around Gemini as the narrative generation engine.

Future versions may add a model-provider layer so SproutAgent can support other approved models without rebuilding the workflow.

The long-term goal is not to tie the product to one model. The goal is to build reusable finance workflows where the AI model is one interchangeable part of the system.

## Local Setup Notes

Create a local `.env` file using `.env.example` and add your Gemini API key there.

Do not commit `.env` to GitHub.

Example:

```bash
GEMINI_API_KEY=your_real_key_here
GEMINI_MODEL=gemini-1.5-flash
REPORT_OUTPUT_DIR=reports
```

## Human Review Principle

SproutAgent is a copilot and execution assistant. It is not a final decision-maker.

All AI-generated finance narratives, reporting outputs, and recommendations should be reviewed, edited, and approved by a human consultant or finance professional before use.

## Long-Term Vision

SproutAgent begins as a mock consulting simulation, but the long-term vision is a realistic finance execution prototype that helps CFO and FP&A teams automate repeatable reporting workflows, standardize outputs, and turn structured data into decision-ready narratives.

## Contact

**Caitlin Przywara**  
GitHub: @Isap31
