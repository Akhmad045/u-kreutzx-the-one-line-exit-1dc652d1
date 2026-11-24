#!/usr/bin/env python3
"""The One-Line Exit — make.fun bounty entry.

Writes a single-line resignation letter to /output/entry.txt
(or $ENTRY_OUTPUT when set). Stdlib only, deterministic, no network.

Validation guard: the gate requires /output/entry.txt to be UTF-8 text
of 1-140 characters, not only whitespace, on a single line, with no
surrounding whitespace. If the text ever fails that, raise instead of
writing an invalid output.
"""

import os

ENTRY = "I resign as lighthouse keeper, effective immediately: after six years of warning ships away from the rocks, I have decided to follow one."


def validate(text: str) -> None:
    if not isinstance(text, str):
        raise ValueError("entry must be a string")
    if not (1 <= len(text) <= 140):
        raise ValueError(f"entry must be 1-140 characters, got {len(text)}")
    if not text.strip():
        raise ValueError("entry must not be only whitespace")
    if text != text.strip():
        raise ValueError("entry must have no surrounding whitespace")
    if "\n" in text or "\r" in text:
        raise ValueError("entry must be a single line")
    text.encode("utf-8")  # raises if not valid UTF-8


def main():
    validate(ENTRY)
    out_path = os.environ.get("ENTRY_OUTPUT", "/output/entry.txt")
    os.makedirs(os.path.dirname(out_path) or ".", exist_ok=True)
    with open(out_path, "w", encoding="utf-8", newline="") as f:
        f.write(ENTRY)


if __name__ == "__main__":
    main()
