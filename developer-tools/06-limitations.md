# 6. Limitations — and why Day 24 exists

CrewAI is the easiest framework to read. That is its strength. These are
the honest limits you will meet on a real project.

| Limit | What it means in practice |
|---|---|
| **No checkpoints** | If the run fails at the last task, everything before it is lost. You run — and pay for — the whole crew again |
| **Little control over the conversation** | You describe roles and order. You don't control exactly how agents exchange information |
| **A weak first task spoils everything** | A wrong fact from the researcher is passed on, and the writer trusts it |
| **Cost grows with the notes** | Everything one task writes goes into the next task's input |
| **Memory is off by default** | Each `kickoff()` starts fresh |
| **Errors can be unclear** | When something fails mid-crew, the message often says *that* it failed more clearly than *why* |

## What real teams do

> Build a first version in CrewAI, to check the idea works. Then rebuild the
> parts that matter in LangGraph, which can save progress, recover from
> errors, and show exactly what happened.

You will see these limits for yourself on Day 24, and meet LangGraph on
Day 25.
