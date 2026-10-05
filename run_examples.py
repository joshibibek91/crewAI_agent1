"""
Run the travel crew on several destinations, and save each result.
==================================================================

    python run_examples.py          run all five, one after another
    python run_examples.py 2        run only example 2

Each finished travel piece is saved in the outputs/ folder, so you can
open them side by side and compare.

The crew itself is in travel_crew.py. This file only feeds it different
inputs — notice that travel_crew.py never changes. That is the point of
the {destination} placeholder.
"""

import sys
from pathlib import Path

from travel_crew import crew

EXAMPLES = [
    ("Bandipur", "A well-known hilltop town. The crew should find plenty."),
    ("Pokhara", "A big tourist city. Watch how many searches the researcher makes."),
    ("Lumbini", "A famous heritage site. Check that every fact has a source link."),
    ("Ilam", "Less information online. Some facts may come back as 'not found'."),
    ("Shangri-Bazaar, Nepal",
     "A MADE-UP place. An honest crew should say it could not find it, "
     "not invent facts about it."),
]

OUTPUT_FOLDER = Path(__file__).parent / "outputs"


def run(index: int) -> None:
    destination, note = EXAMPLES[index]
    print("\n" + "=" * 70)
    print(f"EXAMPLE {index + 1}:  {destination}")
    print(f"What to look for: {note}")
    print("=" * 70)

    result = crew.kickoff(inputs={"destination": destination})

    OUTPUT_FOLDER.mkdir(exist_ok=True)
    file_name = destination.split(",")[0].lower().replace(" ", "-") + ".md"
    path = OUTPUT_FOLDER / file_name
    path.write_text(f"# {destination}\n\n{result.raw}\n", encoding="utf-8")

    print(f"\nSaved to: outputs/{file_name}")
    print(f"Tokens used: {result.token_usage.total_tokens}")


if __name__ == "__main__":
    if len(sys.argv) > 1:
        run(int(sys.argv[1]) - 1)
    else:
        for i in range(len(EXAMPLES)):
            run(i)
