#!/usr/bin/env python3
"""Entry for 'One-Line Office Joke: 24-Hour Sprint'
(u-pucuys-one-line-office-joke-24-hour-sprint-aaf86162).

Writes one short joke about office life to /output/entry.txt: the
office plant died, and facilities answered with a framed photo of a
plant plus a memo about resilience. Stdlib only; no path depends on
the working directory. The output path can be overridden with an
argument or the ENTRY_OUTPUT environment variable, which only exists
so the entry can be verified locally without touching /output.
"""

import os
import sys

LINE = (
    "The office plant died, so facilities replaced it with a framed "
    "photo of a plant and a memo about resilience."
)


def output_path():
    if len(sys.argv) > 1:
        return sys.argv[1]
    return os.environ.get("ENTRY_OUTPUT", "/output/entry.txt")


def main():
    if not 1 <= len(LINE) <= 200:
        raise SystemExit("entry line must be 1 to 200 characters")
    path = output_path()
    parent = os.path.dirname(path)
    if parent:
        os.makedirs(parent, exist_ok=True)
    with open(path, "w", encoding="utf-8") as f:
        f.write(LINE)


if __name__ == "__main__":
    main()
