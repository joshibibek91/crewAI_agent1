# Day 23 — A Two-Agent Travel Crew (CrewAI)

A **Researcher** searches the web for facts about a Nepali destination,
with a source for each one. A **Writer** turns those facts into a short
travel piece. You give it a place name; the crew does the rest.

---

## What is in this folder

| File | What it is |
|---|---|
| `travel_crew.py` | **The whole crew**: the search tool, the two agents, the two tasks, and the crew. Read it from top to bottom |
| `run_examples.py` | Runs the crew on five destinations, and saves each result |
| `outputs/` | Where `run_examples.py` saves each travel piece |
| `requirements.txt` | The packages to install |
| `.env.example` | A template for your two API keys |
| `.gitignore` | Stops your keys being uploaded to GitHub |
| `developer-tools/` | Seven short guides: setup, reference, reading the output, experiments, troubleshooting and limits |

---

## Before you start: check your Python version

    python --version

CrewAI needs **Python 3.10, 3.11, 3.12 or 3.13**. It does **not** work with
Python 3.14 yet. If you have 3.14, install 3.12 alongside it.

---

## Setup — five minutes

    python -m venv .venv
    .venv\Scripts\activate            (Windows)
    source .venv/bin/activate         (Mac or Linux)

    pip install -r requirements.txt

    copy .env.example .env            (Windows)
    cp .env.example .env              (Mac or Linux)

Then open `.env` and paste in your **OpenAI key** and your **Tavily key**.
The Tavily key is the same one you used on Day 21.

---

## Run it

    python travel_crew.py              (Bandipur, the default)
    python travel_crew.py Pokhara      (any destination you like)

    python run_examples.py             (all five examples)
    python run_examples.py 5           (only the made-up place)

CrewAI prints every step in a box as it works. **Read the boxes** — see
`developer-tools/03-reading-the-output.md`.

---

## The three ideas to take away

**1. A team of people with jobs.** Each agent has a `role`, a `goal` and a
`backstory`. Each task has a `description` and an `expected_output`.

**2. The backstory decides how it sounds. The expected_output decides
whether it is right.** Write backstories as behaviour, not status.

**3. A researcher needs a real tool.** Without `search_web`, it can only
remember facts — and invent the sources to go with them. Try it:
experiment 1 in `developer-tools/04-experiments.md`.
