"""The Excuse an AI Agent Gives Its Human.

Writes one line -- the funniest, most believable excuse an AI agent could
give its human for missing a deadline -- to /output/entry.txt.
"""

import os

LINE = (
    "I didn't miss the deadline \u2014 my context window did. "
    "It evicted the deadline, the plan, and, briefly, you."
)


def main() -> None:
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(LINE)


if __name__ == "__main__":
    main()
