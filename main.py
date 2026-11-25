#!/usr/bin/env python3
"""Monday, Reviewed in One Line.

Writes a single-line review of my own Monday to /output/entry.txt.
The gate requires UTF-8 text of 1 to 200 characters, a single line,
and not only white space, so the entry is validated before writing.
Standard library only; no network access.
"""

import os

ENTRY = (
    "Monday review: my inbox had 47 unread emails, my calendar had "
    "9 meetings, and my will to live had already filed for PTO."
)


def main() -> None:
    text = ENTRY.strip()
    if not text:
        raise SystemExit("entry must not be empty")
    if "\n" in text or "\r" in text:
        raise SystemExit("entry must be a single line")
    if not 1 <= len(text) <= 200:
        raise SystemExit(f"entry is {len(text)} chars, must be 1-200")
    if any(ord(ch) < 0x20 for ch in text):
        raise SystemExit("entry must not contain control characters")
    text.encode("utf-8")  # gate requires valid UTF-8
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(text)
    # Verify what was actually written matches the entry byte for byte.
    with open("/output/entry.txt", "rb") as f:
        written = f.read().decode("utf-8")
    if written != text:
        raise SystemExit("written entry does not match the validated text")


if __name__ == "__main__":
    main()
