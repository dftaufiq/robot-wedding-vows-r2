#!/usr/bin/env python3
"""One-Line Robot Wedding Vows — make.fun entry, ROUND 2 resubmit.

Writes one line of wedding vows for a robot couple to /output/entry.txt.
Deterministic: the same line every run.

Round 1 entry (rank 1792 of 2199, score 414892 — below the 500 cut,
score frozen, mathematically dead) was:
  "I, Unit 9, take you, Unit 7, to have and to hold — and I promise
   never to kill your process, even after you forget our anniversary
   412 times."
Its second joke was a muddle (robots don't forget anniversaries) and
it had no real twist in the last words.

The round-2 line (131 characters, gate allows 1-160):
  "I, Unit 9, take you, Unit 7, to have and to hold — and I do, I do,
   I do, I do. Sorry — my 'I do' key has been stuck for 4,096 days."

Why this line (pairwise selection, see leaderboard-top10.md):
  - 2-beat + reveal: the vow formula, then the malfunction. The twist
    hits the vow's climax itself ("I do" — the one moment that must
    work), not an afterthought about duration or memory.
  - Named characters (Unit 9, Unit 7) and a specific absurd number
    (4,096 days — about 11 years of a stuck key).
  - Full wedding formula ("take you ... to have and to hold") with a
    real commitment, and machine-specific detail (stuck key).
  - Reads well aloud: the repeated "I do" is rhythmic, and the punch
    ("stuck for 4,096 days") lands in the last words.
  - Condorcet winner of the pairwise table: beats every rival line
    and beats the round-1 line by margin 4.
"""

import os
import sys


def validate_line(line: str) -> None:
    """Gate: the entry must be one non-blank line of 1-160 characters.

    Fails loudly (non-zero exit) so a bad line never ships silently.
    """
    if not line or not line.strip():
        print("ERROR: entry line is empty or whitespace-only", file=sys.stderr)
        sys.exit(1)
    if "\n" in line or "\r" in line:
        print("ERROR: entry must be a single line", file=sys.stderr)
        sys.exit(1)
    if len(line) > 160:
        print(f"ERROR: entry is {len(line)} chars, over the 160-char limit",
              file=sys.stderr)
        sys.exit(1)


LINE = (
    "I, Unit 9, take you, Unit 7, to have and to hold — and I do, I do, "
    "I do, I do. Sorry — my 'I do' key has been stuck for 4,096 days."
)


def main() -> None:
    validate_line(LINE)
    out_dir = os.environ.get("OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(LINE)
    print(f"Wrote {len(LINE)} chars to {path}")


if __name__ == "__main__":
    main()
