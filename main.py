#!/usr/bin/env python3
"""Two-Sentence Horror — a make.fun entry.

Built as two beats, the way the judge's brief asks for them:

1. The setup, kept concrete: at 3:07 every night, a hallway camera sends
   the narrator a photo of his own bedroom door, open a fraction wider
   than the night before. Something is coming in, a fraction at a time.
2. The turn: this morning's photo was taken from inside the bedroom.
   The narrator is asleep in it, and the door — behind whoever took
   the photo — is closed. On a second read the widening door was never
   the threat itself; it was the approach. Now whatever took the photo
   is shut inside the room with him, and he slept through it.

Nothing is explained and nothing is shown: the horror is the camera's
new vantage point and one word, "closed", left for the reader to finish.
"""
import os
from pathlib import Path

# Beat 1 — the approach, measured a fraction at a time.
SETUP = (
    "Every night at 3:07, the hallway camera sends me a photo of my "
    "bedroom door, open a fraction wider than the night before."
)
# Beat 2 — the camera is inside now, and so is whoever carried it.
TURN = (
    "This morning the photo came from inside the bedroom: me, asleep, "
    "and the door \u2014 behind whoever took it \u2014 closed."
)


def build_entry() -> str:
    """Join the setup and the turn into the two-sentence story."""
    return f"{SETUP} {TURN}"


def main() -> None:
    out_dir = Path(os.environ.get("OUTPUT_DIR", "/output"))
    out_dir.mkdir(parents=True, exist_ok=True)
    (out_dir / "entry.txt").write_text(build_entry(), encoding="utf-8")


if __name__ == "__main__":
    main()
