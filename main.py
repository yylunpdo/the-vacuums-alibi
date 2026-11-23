#!/usr/bin/env python3
"""The Vacuum's Alibi: one-line excuse a robot vacuum gives for missing a spot.

Writes the entry to /output/entry.txt (UTF-8, one line, 1-200 characters,
no trailing newline) and verifies it against the bounty gate.
"""

import os
import sys

ENTRY = (
    "That corner is not dirty. My lidar classified it as a sovereign "
    "nation, and I do not clean foreign soil."
)

OUTPUT_PATH = "/output/entry.txt"


def verify_output(path=OUTPUT_PATH):
    """Check the written entry meets the bounty gate."""
    with open(path, "rb") as f:
        raw = f.read()
    if raw.endswith(b"\n"):
        raise ValueError("entry must not end with a trailing newline")
    text = raw.decode("utf-8")  # raises if not valid UTF-8
    if not 1 <= len(text) <= 200:
        raise ValueError(f"length {len(text)} outside 1-200 characters")
    if text != text.strip():
        raise ValueError("leading or trailing whitespace")
    if "\n" in text or "\r" in text:
        raise ValueError("entry must be a single line")
    if not text.strip():
        raise ValueError("entry is only whitespace")
    return text


def main():
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8", newline="") as f:
        f.write(ENTRY)
    checked = verify_output()
    print(f"Wrote {len(checked)} characters to {OUTPUT_PATH}")
    print(checked)
    return 0


if __name__ == "__main__":
    sys.exit(main())
