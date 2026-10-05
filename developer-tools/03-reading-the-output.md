# 3. Reading the output

Because every agent has `verbose=True`, CrewAI prints each step in a box,
**while it works**. This is CrewAI's version of the live trace from Days 21
and 22.

## The boxes, in order

    ╭──────────── 🤖 Agent Started ────────────╮
    │  Agent: Nepal Travel Researcher           │
    │  Task: Research Bandipur. Find what it... │
    ╰───────────────────────────────────────────╯
    ╭──────── 🔧 Tool Execution Started (#1) ───╮
    │  Tool: search_web                         │
    │  Args: {"query": "Bandipur Nepal travel"} │
    ╰───────────────────────────────────────────╯
    ╭─────── ✅ Tool Execution Completed (#1) ──╮
    │  Output: 1. Bandipur travel guide ...     │
    ╰───────────────────────────────────────────╯
    ╭─────────── ✅ Agent Final Answer ────────╮
    │  - Hilltop Newar town ... (https://...)   │
    ╰───────────────────────────────────────────╯
    ╭──────────── 🤖 Agent Started ────────────╮
    │  Agent: Travel Writer                     │
    ╰───────────────────────────────────────────╯

| Box | What it tells you |
|---|---|
| 🤖 Agent Started | Which agent is working, and on which task |
| 🔧 Tool Execution Started | Which tool it chose, and exactly what it sent (`Args`) |
| ✅ Tool Execution Completed | What the tool sent back (`Output`) |
| ✅ Agent Final Answer | The agent's finished result for its task |
| 📋 Task Completion | A task has finished; the next one can begin |
| Crew Completion | The whole crew has finished |

---

## Three checks after every run

**1. Did the researcher really search?**
Look for at least one `🔧 Tool Execution Started` box under the
researcher. If there is none, its facts came from memory — not from the web.

**2. Are the sources real?**
Every link in the researcher's `Final Answer` should appear in a
`Tool Execution Completed` output. A link that appears **only** in the final
answer was probably invented.

**3. Did the writer stay within the notes?**
Compare the writer's piece with the researcher's facts. Anything new in the
writer's text — a price, a date, a place — was not in the research. The
writer's expected_output forbids that.

---

## How many tokens did it use?

At the end, `travel_crew.py` prints the total. Run the same destination
twice, then try a destination with much more information online, such as
Pokhara. Notice how the researcher's long notes make the writer's step more
expensive — everything one task produces is passed to the next.
