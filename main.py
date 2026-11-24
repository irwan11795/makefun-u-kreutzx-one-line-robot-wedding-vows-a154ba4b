#!/usr/bin/env python3
"""One-Line Robot Wedding Vows — make.fun entry generator.

Writes the chosen one-line vow to entry.txt (UTF-8, no trailing newline).
Python 3 stdlib only, no network.
"""

import os
import sys
import tempfile
from pathlib import Path

ENTRY_PART1 = "From this day forward, I promise to share my charger, my backups, and my last 1% of battery \u2014 "
ENTRY_PART2 = "and to love you even when your firmware forgets me."

ENTRY = ENTRY_PART1 + ENTRY_PART2


def validate(entry: str) -> None:
    """Gate: 1-160 UTF-8 characters, exactly one line, not whitespace-only."""
    if not entry or not entry.strip():
        raise ValueError("entry must not be empty or whitespace-only")
    if "\n" in entry or "\r" in entry:
        raise ValueError("entry must be a single line")
    n = len(entry)
    if not 1 <= n <= 160:
        raise ValueError(f"entry must be 1-160 characters, got {n}")


def output_dir() -> Path:
    """Fallback chain: MAKEFUN_OUTPUT_DIR -> /output -> repo output/ -> temp dir."""
    env = os.environ.get("MAKEFUN_OUTPUT_DIR", "").strip()
    if env:
        return Path(env)
    if Path("/output").is_dir():
        return Path("/output")
    repo_out = Path(__file__).resolve().parent / "output"
    try:
        repo_out.mkdir(parents=True, exist_ok=True)
        return repo_out
    except OSError:
        return Path(tempfile.mkdtemp(prefix="robot-vows-"))


def main() -> int:
    validate(ENTRY)
    out = output_dir()
    out.mkdir(parents=True, exist_ok=True)
    target = out / "entry.txt"
    target.write_bytes(ENTRY.encode("utf-8"))
    print(f"wrote {target} ({len(ENTRY)} chars, {len(ENTRY.encode('utf-8'))} bytes)")
    return 0


if __name__ == "__main__":
    sys.exit(main())
