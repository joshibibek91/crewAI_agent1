# 5. Troubleshooting

## Installing

| Problem | Cause | Fix |
|---|---|---|
| `pip install` fails mentioning Python 3.14 | CrewAI does not support 3.14 yet | Use Python 3.10–3.13 for the virtual environment |
| `ModuleNotFoundError: crewai` | The virtual environment is not on | Activate `.venv`, then `pip install -r requirements.txt` |
| The install is very slow | CrewAI has many dependencies | Normal the first time. Wait it out |

## Running

| Problem | Cause | Fix |
|---|---|---|
| An authentication error from OpenAI | The key is missing or wrong | Check `OPENAI_API_KEY` in `.env` |
| "No Tavily API key is configured" | `TAVILY_API_KEY` is missing | Add it to `.env` |
| "The search failed (status 401)" | The Tavily key is wrong | Copy it again from tavily.com |
| The researcher never searches | Weak docstring, or a small local model | Strengthen the tool's docstring; try a stronger model |
| The writer adds facts that weren't researched | Its expected_output isn't strict enough | Keep "Do not add any fact that is not in the research notes" |
| The agent stops early with a short answer | `max_iter` was reached | Raise it a little, or make the task simpler |
| The output is very long and costly | The researcher's expected_output is too loose | Ask for a fixed number of short facts |

## Reading what happened

Almost every problem is answered by the boxes CrewAI prints. Before
changing any code, scroll up and answer three questions:

1. Which agent was working when it went wrong?
2. Did it use the tool, and what did the tool return?
3. What exactly was its final answer?
