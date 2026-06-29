# Advisor Brief — LLM-Powered Pre-Meeting Briefing Tool

A Python prototype that uses the Anthropic Claude API to generate 
pre-meeting briefs and follow-up questions for financial advisors 
based on client profile data.

## What it does

- Generates a structured pre-meeting summary with key talking points
- Suggests 3 tailored follow-up questions for the advisor to ask
- Built as a feasibility experiment in AI-assisted advisor workflows

## Tech

- Python 3.11
- Anthropic Claude API (claude-sonnet-4-6)

## Setup

1. Clone the repo
2. Create a virtual environment: `python3 -m venv venv`
3. Activate it: `source venv/bin/activate`
4. Install dependencies: `pip install anthropic`
5. Set your API key: `export ANTHROPIC_API_KEY="your-key-here"`
6. Run: `python3 advisor_brief.py`
