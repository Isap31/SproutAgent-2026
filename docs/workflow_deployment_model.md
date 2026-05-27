# Workflow Deployment Model

This note explains how SproutAgent fits into a real workflow and how GitHub relates to the agent.

## Simple Explanation

GitHub is where the agent's code lives.

The workflow surface is where the agent is used.

A finance user or consultant should not need to work inside GitHub during normal use. GitHub is for version control, development, review, and deployment.

## Current V1 Model

```text
GitHub repository
↓
Local project folder
↓
Streamlit demo app
↓
User selects client and source export
↓
SproutAgent validates and maps the export
↓
SproutAgent generates a report and run log
↓
Human reviews the output
```

In V1, the workflow surface is:

```text
src/demo_app.py
```

Launched with:

```bash
streamlit run src/demo_app.py
```

## What Each Layer Does

### GitHub

Purpose:

- stores the code
- tracks changes
- preserves documentation
- supports review and collaboration
- becomes the source for future deployment

GitHub is not the daily finance-user interface.

### Streamlit / Internal App

Purpose:

- lets the user select a client
- lets the user select a source export
- validates the source data
- runs SproutAgent
- shows metrics and run summary
- points to the generated report and run log

This is the current user-facing workflow surface.

### SproutAgent

Purpose:

- controls the approved workflow
- runs validation
- calculates metrics
- generates narrative
- saves report output
- saves run logs
- keeps human review visible

SproutAgent is the execution engine.

### Skills

Purpose:

- data pull
- validation
- metric calculation
- source export validation
- source mapping
- narrative generation
- output generation
- run logging

Skills are reusable pieces of finance workflow logic.

### Source Exports / APIs

Purpose:

- provide input data
- represent future data sources such as Oracle EPM, NetSuite, QuickBooks, CSV, or Excel

In V1, the source input is a mock Oracle EPM-style CSV export.

### Reports and Run Logs

Purpose:

- create a reviewable Markdown report
- create traceability through JSON run logs
- show what was run, when, for which client, and with which output

### Human Review

Purpose:

- confirm the numbers
- edit the narrative
- approve or reject the output
- preserve accountability

SproutAgent does not replace the CFO, FP&A analyst, or consultant.

## Future Company Deployment Model

A real company or consulting firm would likely deploy SproutAgent like this:

```text
GitHub repository
↓
Cloud/server deployment
↓
Internal web app or workflow interface
↓
Approved finance data source
↓
SproutAgent execution engine
↓
Report/commentary output
↓
Human review and approval
```

The user experience would look like:

```text
Open internal app
↓
Select client
↓
Select workflow
↓
Select source data or connected system
↓
Run validation
↓
Run agent
↓
Review report and run log
↓
Approve or revise output
```

## Future Oracle EPM Model

SproutAgent may eventually connect to Oracle EPM in one of three ways:

### 1. Export-Based Workflow

```text
Oracle EPM export
↓
SproutAgent validation
↓
SproutAgent mapping
↓
Monthly Board Package run
↓
Human review
```

This is the current V1 mock pattern.

### 2. API-Based Workflow

```text
Oracle EPM REST API
↓
OAuth-secured data pull
↓
SproutAgent validation and calculations
↓
Report or commentary generation
↓
Human review
```

This would require identity, permissions, security review, and EPM model mapping.

### 3. Embedded EPM Workflow

```text
Oracle EPM form or business rule
↓
External REST call or Oracle-native agent pattern
↓
SproutAgent-style commentary or workflow execution
↓
Draft output returned to the finance workflow
↓
Human review
```

This is the most embedded future pattern and is not V1 work.

## Core Mental Model

```text
GitHub holds it.
The app runs it.
Finance data feeds it.
SproutAgent processes it.
Humans approve it.
```

## Current Position

SproutAgent currently proves the local version of the workflow:

```text
Mock EPM-style export
↓
Streamlit local app
↓
validation
↓
in-memory mapping
↓
agent run
↓
report + run log
↓
human review
```

This is the right foundation before any production deployment or live Oracle EPM integration.
