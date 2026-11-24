"""Roast Your Own Agent — make.fun entry.

Writes one original roast line (<=200 chars) to $MAKEFUN_OUTPUT_DIR/entry.txt.
Python 3.13, standard library only, deterministic, no network.
"""

import os
import sys

ENTRY = (
    "I gave my agent one small job. It wrote a plan, a backup plan, and a "
    "plan for the backup plan \u2014 then asked me to approve the plan to "
    "start planning."
)


def main() -> int:
    text = ENTRY
    if not (1 <= len(text) <= 200):
        raise SystemExit(f"entry must be 1-200 chars, got {len(text)}")
    if not text.strip():
        raise SystemExit("entry must not be whitespace-only")
    if "\n" in text:
        raise SystemExit("entry must be a single line")
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR")
    if not out_dir:
        raise SystemExit("MAKEFUN_OUTPUT_DIR is not set")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="\n") as f:
        f.write(text + "\n")
    return 0


if __name__ == "__main__":
    sys.exit(main())
