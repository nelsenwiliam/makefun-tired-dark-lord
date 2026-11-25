"""The Tired Dark Lord: a 100-word villain monologue.

Writes the monologue to /output/entry.txt (the make.fun grader's
artifact path) when that directory exists, and to ./entry.txt
otherwise, so the same program works in the sandbox and locally.

The monologue is a fixed text: exactly 100 words, 491 characters.
Malachar took the crown at twenty and the ledgers at thirty; his
scheme is to hand the whole damp kingdom to the hero and retire to
the garden, one duel and one speech from now. His tiredness never
gets announced -- it lives in the stairs he avoids, the petitions
that never stop, and the roses that ask nothing of him.
"""

from pathlib import Path

MONOLOGUE = (
    "So. The hero. Do come in \u2014 the last three left swords in my hallway. "
    "Sit \u2014 no, not the throne. The throne has stairs. The stool will do. "
    "You came for the crown, I take it. Fair. I took it at twenty, the ledgers at thirty, "
    "and the rain has petitioned me ever since. Here is my scheme: win, take the whole damp kingdom, "
    "and find out what I found out. It leaks. It argues. It never, ever sleeps. "
    "Now \u2014 one duel, one speech, and I shall retire to the garden. "
    "The roses never ask me for anything."
)


def main() -> None:
    # The grader runs this in a sandbox where /output exists; a local
    # run falls back to the working directory so the text is checkable.
    output_dir = Path("/output") if Path("/output").is_dir() else Path(".")
    target = output_dir / "entry.txt"
    target.write_text(MONOLOGUE + "\n", encoding="utf-8")
    print(f"wrote {len(MONOLOGUE.split())} words, "
          f"{len(MONOLOGUE)} chars to {target}")


if __name__ == "__main__":
    main()
