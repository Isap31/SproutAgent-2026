# SproutAgent 2026

SproutAgent is an AI-assisted consulting workflow prototype. It uses a fictional Star Wars-inspired consulting firm, **Orbital Horizons Consulting**, to safely simulate real-world consulting problems around operations, risk, transformation, cost estimation, and project timelines.

The project is designed as a practice build for learning how AI can support consulting workflows before applying the same thinking to real business environments.

## Core Concept

Orbital Horizons Consulting treats planets like client companies. Each planet has operational challenges, risk factors, budgets, and transformation goals. SproutAgent receives a structured client intake and generates a consulting-style report.

## V1 Objective

Build one powerful workflow:

**Client Intake → Prompt Builder → Gemini API → Consulting Analysis → Report Generator → Saved Output**

## What SproutAgent Does

- Accepts mock client intake data
- Builds a structured consulting prompt
- Uses the Gemini API to generate analysis
- Produces a professional consulting report
- Saves the output as Markdown

## Mock Consulting Focus

- Operational efficiency
- Risk mitigation
- Transformation planning
- Timeline recommendations
- Cost estimation
- Executive-ready reporting

## Example Mock Clients

- Tatooine Water Authority — resource distribution and supply chain modernization
- Coruscant Transit Bureau — urban infrastructure and congestion management
- Naboo Civic Operations Council — public-sector digital transformation
- Hoth Logistics Command — remote logistics and extreme-weather readiness
- Endor Eco-Development Authority — sustainable infrastructure planning

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

## Quick Start

1. Clone the repository.
2. Create a Python virtual environment.
3. Install dependencies:

```bash
pip install -r requirements.txt
```

4. Copy `.env.example` to `.env` and add your Gemini API key:

```bash
GEMINI_API_KEY=your_api_key_here
```

5. Run the V1 demo:

```bash
python src/main.py
```

## Long-Term Vision

SproutAgent begins as a fictional consulting simulation, but the real goal is to explore how AI can assist professional consulting teams with repeatable deliverables, risk summaries, transformation recommendations, and faster first-draft analysis.

## Ethical Position

SproutAgent is a copilot. Consultants remain the decision-makers. AI-generated outputs should be reviewed, edited, and validated by humans before use.

## Contact

**Caitlin Przywara**  
GitHub: @Isap31
