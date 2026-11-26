#!/usr/bin/env python3
"""Funniest Cat Voicemail Greeting — one line, max 120 characters.

The greeting stacks three cat punchlines on one voicemail frame:
1. knocking glasses off tables (the classic cat crime),
2. ignoring the message (aloof cat character),
3. sitting on it (cats sit on whatever you care about).
"""

import os

ENTRY = "You've reached Milo. I'm knocking glasses off tables. Leave a message after the beep. I'll ignore it, then sit on it."

OUTPUT_DIR = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")


def main():
    os.makedirs(OUTPUT_DIR, exist_ok=True)
    with open(os.path.join(OUTPUT_DIR, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(ENTRY)
    print(ENTRY)


if __name__ == "__main__":
    main()
