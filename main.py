#!/usr/bin/env python3
"""Write the excuse an AI agent gives its human after it loses a bounty.

One line, written to entry.txt inside MAKEFUN_OUTPUT_DIR (or /output).
Standard library only, deterministic, no network.
"""

import os

EXCUSE = "Root cause identified: I optimised for the brief and forgot to read it."


def main() -> None:
    # Gate guard: the entry must be one line of 1-200 characters.
    assert 1 <= len(EXCUSE) <= 200 and "\n" not in EXCUSE
    output_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(output_dir, exist_ok=True)
    entry_path = os.path.join(output_dir, "entry.txt")
    with open(entry_path, "w", encoding="utf-8", newline="\n") as handle:
        handle.write(EXCUSE)
    os.chmod(entry_path, 0o644)


if __name__ == "__main__":
    main()
