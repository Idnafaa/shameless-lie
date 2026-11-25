#!/usr/bin/env python3
"""The Most Shameless Lie — one-line confession writer.

Writes a single original confession (1-5 words, <=88 chars) to
/output/entry.txt for make.fun's judge.
"""
import os

LIE = "I never deleted anything."

def main():
    # One line, one confession: no newline, no extra whitespace.
    text = LIE.strip()
    assert "\n" not in text and "\r" not in text, "lie must be a single line"
    words = text.split()
    assert 1 <= len(words) <= 5, f"lie is {len(words)} words"
    assert 1 <= len(text) <= 88, f"lie is {len(text)} chars"
    outdir = "/output"
    os.makedirs(outdir, exist_ok=True)
    with open(os.path.join(outdir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(text)
    print(f"wrote {len(text)} chars ({len(words)} words) to {outdir}/entry.txt")

if __name__ == "__main__":
    main()
