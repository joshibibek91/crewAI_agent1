"""
Day 23 — A two-agent travel crew (CrewAI)
=========================================

A Researcher finds facts about a Nepali destination, with sources.
A Writer turns those facts into a short travel piece.

Run it:   python travel_crew.py
          python travel_crew.py Pokhara

Needs in .env:   OPENAI_API_KEY   and   TAVILY_API_KEY
"""

import os
import sys

import requests
from dotenv import load_dotenv
from crewai import Agent, Task, Crew, Process, LLM
from crewai.tools import tool

load_dotenv()


# ---------------------------------------------------------------------------
# The Researcher's tool: web search.
# The same Tavily search as Day 21. Without a tool, a researcher can only
# "remember" facts — and invent the sources to go with them.
# ---------------------------------------------------------------------------

@tool("search_web")
def search_web(query: str) -> str:
    """Search the web for current facts about a place in Nepal.
    Use it for every fact you report. It returns up to 5 results, each with a
    title, a link and a short summary. If nothing is found, it says so: then
    write "not found" rather than guessing."""
    key = os.getenv("TAVILY_API_KEY")
    if not key:
        return "No Tavily API key is configured, so the search could not run."
    try:
        response = requests.post(
            "https://api.tavily.com/search",
            headers={"Authorization": f"Bearer {key}"},
            json={"query": query, "max_results": 5},
            timeout=15,
        )
    except requests.RequestException as error:
        return f"Could not reach the search service: {error}"

    if response.status_code != 200:
        return f"The search failed (status {response.status_code})."
    results = response.json().get("results", [])
    if not results:
        return "No results were found for that search."

    lines = []
    for i, r in enumerate(results, start=1):
        summary = (r.get("content") or "")[:300]
        lines.append(f"{i}. {r.get('title')}\n   {r.get('url')}\n   {summary}")
    return "\n\n".join(lines)


# ---------------------------------------------------------------------------
# The model. Named here, so you can see what runs and what it costs.
# ---------------------------------------------------------------------------

llm = LLM(model="gpt-4o-mini", temperature=0.2)


# ---------------------------------------------------------------------------
# The two agents: the people you "hire".
# Backstories describe BEHAVIOUR, not status (the Day 9 lesson).
# max_iter is each agent's step limit (course rule 3). The default is 25.
# ---------------------------------------------------------------------------

researcher = Agent(
    role="Nepal Travel Researcher",
    goal="Find current facts about {destination}, each with a source",
    backstory=(
        "You never repeat a claim you cannot point to a source for. "
        "You say plainly when you could not find something."
    ),
    tools=[search_web],
    llm=llm,
    max_iter=5,
    allow_delegation=False,
    verbose=True,
)

writer = Agent(
    role="Travel Writer",
    goal="Write a short, warm travel piece about {destination}",
    backstory=(
        "You write short, clear sentences for first-time visitors. "
        "You use only the facts in the research notes, and give prices in NPR."
    ),
    llm=llm,
    max_iter=3,
    allow_delegation=False,
    verbose=True,
)


# ---------------------------------------------------------------------------
# The two tasks: the jobs you give them.
# expected_output is where the accuracy lives (the Day 10 Type letter).
# ---------------------------------------------------------------------------

research_task = Task(
    description=(
        "Research {destination}. Find what it is known for, the best months "
        "to visit, and roughly what a traveller should budget per day in NPR."
    ),
    expected_output=(
        "A bullet list of 5 facts. Each fact must end with its source URL. "
        "If you cannot find something, write: not found."
    ),
    agent=researcher,
)

write_task = Task(
    description=(
        "Write a short travel piece about {destination} for a first-time "
        "visitor, using only the research notes."
    ),
    expected_output=(
        "Three short paragraphs, under 150 words in total. "
        "Do not add any fact that is not in the research notes."
    ),
    agent=writer,
)


# ---------------------------------------------------------------------------
# The crew: the team, and how it works.
# Sequential: research first, then writing. The research result is passed to
# the writer automatically.
# ---------------------------------------------------------------------------

crew = Crew(
    agents=[researcher, writer],
    tasks=[research_task, write_task],
    process=Process.sequential,
    verbose=True,
)


if __name__ == "__main__":
    destination = " ".join(sys.argv[1:]) or "Bandipur"
    result = crew.kickoff(inputs={"destination": destination})

    print("\n" + "=" * 70)
    print("FINAL RESULT")
    print("=" * 70)
    print(result.raw)
    print("\nTokens used:", result.token_usage.total_tokens)
