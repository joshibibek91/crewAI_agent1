# 1. Setup guide

## Requirements

- **Python 3.10, 3.11, 3.12 or 3.13** — CrewAI does not support 3.14 yet.
  Check with `python --version`
- An OpenAI API key
- A Tavily API key (free plan at tavily.com) — the same one as Day 21

---

## Step by step

### 1. A virtual environment

    python -m venv .venv
    .venv\Scripts\activate          (Windows)
    source .venv/bin/activate       (Mac or Linux)

Your terminal line must now start with `(.venv)`.

If `python --version` shows 3.14, create the environment with an older
Python instead. On Windows, if you have 3.12 installed:

    py -3.12 -m venv .venv

### 2. Install

    pip install -r requirements.txt

CrewAI is a large package, so this can take a few minutes the first time.

### 3. `.gitignore` FIRST, then `.env`

`.gitignore` already contains `.env`. Keep it that way, then:

    copy .env.example .env          (Windows)
    cp .env.example .env            (Mac or Linux)

Open `.env` and paste in both keys.

### 4. Run it

    python travel_crew.py

---

## Using your own Ollama model instead

In `travel_crew.py`, replace the `llm = LLM(...)` line with:

    llm = LLM(model="ollama/qwen3:4b", base_url="http://localhost:11434")

Make sure Ollama is running, and that you have pulled the model
(`ollama pull qwen3:4b`). You no longer need the OpenAI key — but you
still need the Tavily key for searching.

**Expect a small local model to use the search tool less reliably.** That
is the Day 4 finding: small models struggle most with following
instructions — and choosing and calling a tool is an instruction.

## Giving each agent a different model

Each agent has its own `llm=` setting. For example, a cheaper model for the
researcher, which mostly gathers facts, and a better one for the writer:

    research_llm = LLM(model="gpt-4o-mini", temperature=0.2)
    writing_llm  = LLM(model="gpt-4o",      temperature=0.5)
