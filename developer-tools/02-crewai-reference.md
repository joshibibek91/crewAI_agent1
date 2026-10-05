# 2. CrewAI reference

Checked against CrewAI version 1.15.

## Agent — the person you hire

    Agent(
        role="Travel Writer",          # job title
        goal="Write a short, warm travel piece about {destination}",
        backstory="You write short, clear sentences...",
        tools=[search_web],            # what it can do
        llm=llm,                       # which model
        max_iter=3,                    # step limit — the default is 25
        allow_delegation=False,        # may it pass work to another agent?
        verbose=True,                  # print every step
    )

| Setting | What it does | Advice |
|---|---|---|
| `role` | The job title | Keep it short |
| `goal` | What the agent tries to achieve | One sentence. Placeholders allowed |
| `backstory` | How the agent behaves. Added to its instructions | Describe **behaviour**, not status (Day 9) |
| `tools` | What the agent can actually do | Give each agent only the tools it needs |
| `llm` | Which model it uses | Name it, so you know the cost |
| `max_iter` | The most steps it may take | **Always set it.** The default is 25 |
| `allow_delegation` | Whether it may hand work to another agent | Off, unless you need it |
| `verbose` | Print every step | On while learning |

## Task — the job you give

    Task(
        description="Research {destination}. Find ...",
        expected_output="A bullet list of 5 facts. Each fact must end with its source URL...",
        agent=researcher,
    )

| Setting | What it does |
|---|---|
| `description` | What to do |
| `expected_output` | **What a finished answer must look like.** Where accuracy comes from |
| `agent` | Who does it |
| `context` | Which earlier tasks' results it should see (Day 24) |

## Crew — the team

    Crew(
        agents=[researcher, writer],
        tasks=[research_task, write_task],
        process=Process.sequential,
        verbose=True,
    )

| Process | What happens |
|---|---|
| `Process.sequential` | Tasks run in the order listed. Each result is passed to the next |
| `Process.hierarchical` | A manager agent decides who does what. Needs `manager_llm` |

These are the only two processes. Start with sequential.

## Starting the crew

    result = crew.kickoff(inputs={"destination": "Bandipur"})

    result.raw                      # the final text
    result.token_usage.total_tokens # tokens used by the whole crew

Every `{destination}` in a goal or description is replaced by the value
you give in `inputs`.

## Tools

A tool is a normal function with `@tool` above it:

    from crewai.tools import tool

    @tool("search_web")
    def search_web(query: str) -> str:
        """The docstring is what the agent reads to decide when to use it."""

To see what the agent is told about a tool:

    python -c "from travel_crew import search_web; print(search_web.description)"
