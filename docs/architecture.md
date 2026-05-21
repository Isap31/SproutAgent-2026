# SproutAgent Architecture

## System Purpose

SproutAgent is an AI-assisted consulting workflow prototype. It receives structured intake information about a fictional planetary client and turns that information into a consulting-style report.

## V1 Pipeline

```text
User Input -> Intake Parser -> Prompt Template -> Gemini API -> Response Formatter -> Report File
```

## Components

### 1. User Input

The user chooses or enters a client scenario. V1 begins with mock JSON data instead of a full web form.

### 2. Intake Parser

The intake parser loads and validates the selected client profile.

### 3. Prompt Builder

The prompt builder combines:

- Prompt template
- Client profile
- Report type
- Consulting instructions

### 4. Gemini Service

The Gemini service sends the prompt to the Gemini API and receives generated analysis.

### 5. Report Generator

The report generator formats the response as Markdown and saves it to the reports folder.

## Repository Structure

```text
sprout-agent/
├── data/
│   ├── planets.json
│   ├── projects.json
│   └── risks.json
├── docs/
│   ├── architecture.md
│   └── roadmap.md
├── prompts/
│   ├── report_prompt.txt
│   ├── risk_prompt.txt
│   └── timeline_prompt.txt
├── reports/
│   └── .gitkeep
├── src/
│   ├── __init__.py
│   ├── gemini_service.py
│   ├── intake.py
│   ├── main.py
│   ├── prompt_builder.py
│   └── report_generator.py
├── .env.example
├── requirements.txt
└── README.md
```

## V1 Design Principles

- Keep the workflow simple.
- Use fake data only.
- Make outputs professional and structured.
- Keep humans responsible for reviewing AI outputs.
- Build one strong workflow before expanding.

## Future Architecture

Future versions may include:

- Streamlit or React frontend
- FastAPI backend
- PDF export
- Client history database
- Multi-agent workflow
- Risk scoring engine
- Proposal generation module
