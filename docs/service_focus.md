# SproutAgent Service Focus

This document defines the service focus for SproutAgent using the fictional consulting firm **Orbital Horizons Consulting**. The service areas are inspired by common CFO and FP&A consulting needs, but the wording, examples, clients, and workflows are specific to this mock project.

## Core Service Areas for Orbital Horizons Consulting

SproutAgent should stay centered on two mock consulting service lines:

1. **Finance Reporting Operations**
2. **Finance Data & Decision Support**

These are recurring, structured, human-reviewed finance workflows. SproutAgent should support controlled execution work, not open-ended autonomous decision-making.

## Service Line 1: Finance Reporting Operations

### Mock Service Description

Orbital Horizons Consulting helps CFO and FP&A teams turn recurring financial reporting work into repeatable, reviewable delivery workflows.

The goal is to reduce manual report preparation, improve consistency, and help consultants create draft outputs faster while keeping humans responsible for final judgment.

### Example Use Cases

- Monthly board package preparation
- Budget vs. actual reporting
- Forecast commentary
- Variance analysis
- Close reporting support
- Executive finance summaries
- Recurring management reporting
- Draft Markdown, PDF, or deck-style outputs

### SproutAgent Role

For this service line, SproutAgent should:

- Load structured client workflow data
- Validate required finance inputs
- Calculate metrics with deterministic code
- Draft CFO-ready commentary with AI support
- Save standardized reporting outputs
- Create run logs for traceability
- Keep every output marked for human review

## Service Line 2: Finance Data & Decision Support

### Mock Service Description

Orbital Horizons Consulting helps finance leaders organize financial and operational data into clearer decision-support outputs.

The goal is to help CFO and FP&A teams understand what changed, why it changed, and what leadership should review next.

### Example Use Cases

- KPI summaries
- Cost driver analysis
- Forecast risk review
- Trend summaries
- Operational finance insights
- Decision-ready executive reporting
- Risk indicators for leadership review

### SproutAgent Role

For this service line, SproutAgent should combine structured data, deterministic calculations, and controlled narrative generation to produce draft insights that a consultant can review, edit, and approve.

## V1 Positioning: Execution Agent

SproutAgent V1 is an execution agent. It is not a fully autonomous agent.

The V1 workflow should remain:

```text
Client workflow data
↓
Data pull skill
↓
Validation skill
↓
Metric calculation skill
↓
Narrative generation skill
↓
Markdown report output
↓
Run log output
↓
Human review
```

Core principle:

```text
Code calculates.
AI narrates.
Humans approve.
```

## Source Data Direction

For the mock version, source data lives in structured JSON files under each client folder.

In a future company-specific implementation, similar source data could come from approved exports from systems such as NetSuite or QuickBooks. SproutAgent would not replace those systems. They would remain the source of record.

Future source path:

```text
Mock JSON data
↓
CSV / Excel exports
↓
NetSuite or QuickBooks exports
↓
Approved API connectors
```

## Skill 001: Monthly Board Package

This is the current V1 skill.

### Inputs

- Client profile
- Reporting period
- Budget
- Actuals
- Forecast
- Prior month actuals
- KPI values
- Cost drivers
- Risk indicators
- Leadership notes

### Outputs

- Executive summary
- Budget vs. actual analysis
- Forecast outlook
- KPI summary
- Cost driver explanation
- Risk summary
- Recommended actions
- CFO decision point
- Draft report for human review
- JSON run log

## Future Skills Parking Lot

These are future skills for Orbital Horizons Consulting, not immediate V1 work.

### Future Skill: Close Reporting Support

Potential outputs:

- Close package draft
- Flux commentary
- Journal review summary
- Cash movement summary
- Open item summary
- Human review checklist

### Future Skill: SaaS KPI Review

Potential outputs:

- ARR movement summary
- Burn multiple review
- CAC / LTV commentary
- Hiring efficiency analysis
- Anomaly flags
- CFO recommendation summary

### Future Skill: Forecast Review

Potential outputs:

- Forecast gap summary
- Risk drivers
- Scenario notes
- Management commentary
- Decision points for leadership

## What V1 Should Not Become Yet

SproutAgent V1 should not become:

- A broad chatbot
- A public SaaS product
- A fully autonomous decision-maker
- A dashboard tool
- A live ERP connector
- A replacement for finance professionals

For now, it should remain focused on one company-specific internal consulting workflow:

```text
CFO / FP&A client folder
↓
Monthly Board Package workflow
↓
Validated metrics
↓
Draft reporting output
↓
Run log
↓
Human review
```

## Demo Positioning

SproutAgent should be presented as a mock internal consulting delivery prototype.

The demo should show how a consulting firm like Orbital Horizons Consulting could use a controlled execution agent to support CFO and FP&A reporting work while preserving structure, traceability, and human review.
