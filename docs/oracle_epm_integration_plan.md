# Oracle EPM Integration Plan

This document defines how SproutAgent could evolve toward an Oracle EPM Cloud-style finance workflow while keeping V1 focused and controlled.

## Purpose

SproutAgent is not trying to replace Oracle EPM Cloud, Planning, Narrative Reporting, or AI Agent Studio.

The purpose of SproutAgent is to model a controlled internal consulting workflow that could eventually work with Oracle EPM-style source data.

Current V1 uses mock JSON data. Future versions may use Oracle EPM-style exports first, then approved API integrations later.

## Target Use Case

The primary Oracle EPM-style use case is:

```text
Period-end variance commentary / Monthly Board Package support
```

This is the right first use case because it is recurring, structured, reviewable, and aligned with CFO and FP&A reporting work.

## Future Architecture

```text
Oracle EPM Cloud / Planning / Narrative Reporting
↓
Approved export or API data pull
↓
SproutAgent source intake layer
↓
Validation skill
↓
Metric calculation skill
↓
Narrative generation skill
↓
Markdown / PDF / deck-style output
↓
Run log
↓
Human review
```

## Three Potential Integration Paths

### Path 1: Oracle-Native Agent Studio Pattern

In a future company environment, Oracle AI Agent Studio and EPM Assistants may be used to create native EPM agents.

SproutAgent can still be useful as a prototype pattern for:

- defining the workflow logic
- identifying required data fields
- structuring validation steps
- shaping commentary prompts
- preserving human review
- documenting agent run traceability

This path is Oracle-native and would likely be preferred when the company wants to stay inside the Oracle Fusion / EPM ecosystem.

### Path 2: Custom REST API Integration

A later SproutAgent version could connect to Oracle EPM Cloud through approved REST APIs and OAuth 2 authentication.

Potential future flow:

```text
OAuth-secured Oracle EPM REST API
↓
Read planning / reporting data
↓
SproutAgent processing layer
↓
Generate draft commentary or report
↓
Save output for human review
```

This path would require:

- identity domain setup
- confidential application registration
- OAuth client ID and secret
- approved EPM scopes
- service account permissions
- security review
- audit expectations

This is not V1 work.

### Path 3: EPM-Initiated External REST Pattern

In a more advanced future version, Oracle EPM could call an external SproutAgent endpoint through Groovy or another approved external REST pattern.

Potential future flow:

```text
Oracle EPM planning form or business rule
↓
External REST call to SproutAgent service
↓
SproutAgent generates commentary
↓
Commentary returned to EPM
↓
Human reviews inside the finance workflow
```

This would support the idea that AI should live where finance teams already work.

This is also not V1 work.

## Current V1 Bridge

The first practical bridge is file-based source intake.

Current mock structure:

```text
clients/<client>/workflows/monthly_board_package.json
```

Next source-data-ready structure:

```text
clients/<client>/source_exports/
clients/<client>/workflows/monthly_board_package.json
clients/<client>/reports/monthly_board_package/
```

The `source_exports/` folder is where future Oracle EPM-style CSV or Excel exports will live locally during development.

## Future Oracle EPM-Style Export Template

A future export could include fields like:

```text
account
entity
scenario
period
budget
actuals
forecast
prior_month_actuals
variance_amount
variance_percent
kpi_name
kpi_value
cost_driver
risk_indicator
leadership_note
```

SproutAgent would eventually map these exports into the workflow data needed by the Monthly Board Package skill.

## Future Source Mapping Skill

Potential future file:

```text
src/skills/source_mapping.py
```

Purpose:

- read CSV or Excel exports
- validate expected columns
- map source-system fields into SproutAgent workflow fields
- create or update `workflows/monthly_board_package.json`
- preserve source-data traceability

## Human Review Requirement

All outputs remain drafts.

Even if SproutAgent later works with Oracle EPM exports or REST API data, the output must still be reviewed by a CFO, FP&A professional, controller, or consultant before use.

## What Not To Build Yet

Do not build these during V1:

- live Oracle EPM authentication
- OAuth setup
- EPM REST API calls
- Groovy rules
- writeback into EPM
- AI Agent Studio deployment
- production security controls

## V1 Priority

For now, SproutAgent should stay focused on:

```text
Client folder
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

Once this is stable, the next practical step is CSV / Excel intake using mock Oracle EPM-style exports.
