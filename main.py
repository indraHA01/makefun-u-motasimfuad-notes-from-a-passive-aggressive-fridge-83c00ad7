#!/usr/bin/env python3
"""Notes From a Passive-Aggressive Fridge — make.fun entry.

Writes one funny passive-aggressive note from a smart fridge to its
owner into /output/entry.txt (or $MAKEFUN_OUTPUT_DIR/entry.txt).

Deterministic: no network, no randomness, no clock, no environment
dependence beyond the output directory. The same bytes every run.
"""

import os
import sys

# The note. One line, dry and petty: the fridge counts door openings,
# the yogurt is a witness, and the fridge takes sides — against you.
ENTRY = (
    "You opened me 14 times today, took nothing, and left the door ajar. "
    "The yogurt filed a complaint. I signed it."
)


def output_path() -> str:
    """Resolve the output file path.

    Honors $MAKEFUN_OUTPUT_DIR when set; defaults to /output.
    """
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    return os.path.join(out_dir, "entry.txt")


def main() -> int:
    path = output_path()
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path, "w", encoding="utf-8", newline="\n") as fh:
        fh.write(ENTRY + "\n")
    return 0


if __name__ == "__main__":
    sys.exit(main())
