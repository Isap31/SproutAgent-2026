# SproutAgent Project Tracker

This file defines the internal project-tracking role for SproutAgent. It is meant to help keep the repository organized as the prototype grows.

## Agent Name

**SproutTracker**

## Core Project Direction

SproutAgent is a mock CFO and FP&A execution-agent prototype for Orbital Horizons Consulting.

The current V1 goal is to prove the Monthly Board Package workflow:

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

## Current Build Focus

Stay focused on hardening V1 before adding additional skills.

Current priority:

1. Keep Monthly Board Package working locally
2. Preserve deterministic metric calculations
3. Improve report traceability
4. Support Gemini live mode with fallback
5. Keep generated reports out of Git
6. Keep `.env` secrets out of Git

## Important Product Principles

- Mock firm, real workflow
- Fake data, serious business problem
- Code calculates
- AI narrates
- Humans approve
- Terminal first, integrations later
- Do not overbuild before V1 is stable

## Future Ideas Parking Lot

These are future ideas, not immediate build tasks:

- Close Reporting skill
- SaaS KPI Review skill
- Excel or CSV input
- PowerPoint output
- Claude provider support
- Model comparison mode
- Excel add-in
- Planning system integration
- AI commentary inside finance workflows

## Update Rule

Whenever a meaningful project change is made, update:

1. `docs/project_status.md`
2. `docs/changelog.md`
3. Relevant README sections only when the project direction changes
