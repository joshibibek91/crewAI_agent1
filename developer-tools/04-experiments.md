# 4. Experiments

Each one teaches something specific. Change **one thing** at a time, then
change it back.

---

## 1. Take away the tool   ★ the most important one

In `travel_crew.py`, remove `tools=[search_web],` from the researcher.
Run it again.

**What you will usually see:** it still produces five facts, *with web
addresses*. Now check them. Some may be wrong, and some links may lead
nowhere.

**Why it matters:** without a tool, the researcher can only remember — and
it invents sources that look real. A source is only real if a tool fetched
it.

---

## 2. Weaken the expected output

Put the tool back. Change the research task's `expected_output` to:

    expected_output="Good research.",

**What you will see:** longer, vaguer notes, often without sources — and a
writer's piece that is worse, because it was built on weaker research.

**Why it matters:** `expected_output` is where accuracy comes from. And a
weak first agent spoils everything after it — the main problem of Day 24.

---

## 3. Turn behaviour into status

Change the researcher's backstory to:

    backstory="You are a world-class expert travel researcher.",

**What you will see:** it may sound more confident — but it is not more
careful about sources, and may be less honest about gaps.

**Why it matters:** the Day 9 lesson. An impressive title changes the tone,
not the accuracy.

---

## 4. Make the step limit too small

Set the researcher's `max_iter=1`.

**What you will see:** it has no room to search *and* answer, so it may
stop early, or answer without searching.

**Why it matters:** limits protect you from runaway cost — but set them
too tight and the agent can't do its job. Find the balance.

---

## 5. Try the made-up place

    python run_examples.py 5

**What you should see:** the researcher finds nothing real, and says so.
The writer then has almost nothing to write about.

**What would be a failure:** a confident travel piece about a place that
does not exist. If you see that, look at the boxes: did the researcher
search, and what did the search return?
