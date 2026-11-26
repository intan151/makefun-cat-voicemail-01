"""Funniest Cat Voicemail Greeting -- write one voicemail greeting recorded
by a cat to /output/entry.txt.

Stdlib only, no network, no randomness: the output is byte-identical on
every run. The greeting keeps the shape of a real voicemail -- a hello,
who is speaking, what to do after the beep -- while the cat's character
does the joking: napping in the thrown-away box, and the 4 a.m. tuna
demand every cat owner recognises.
"""

import os

ENTRY = (
    "Hi, it's Miso. I'm napping in the box you threw away. "
    "Leave a message after the meow \u2014 or just open the tuna at 4 a.m."
)


def main():
    assert 1 <= len(ENTRY) <= 120, "entry must be 1-120 characters"
    assert "\n" not in ENTRY, "entry must be one line"
    assert ENTRY.strip() == ENTRY, "entry must not start or end with space"
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(ENTRY)
    # Read back: the file on disk must be exactly the entry, nothing else.
    with open("/output/entry.txt", "r", encoding="utf-8") as f:
        assert f.read() == ENTRY, "entry.txt does not match the entry"
    # Self-check gate (revision): byte-level re-read must match the entry
    # exactly, and the length must still be inside the 1-120 gate.
    with open("/output/entry.txt", "rb") as f:
        raw = f.read()
    assert raw == ENTRY.encode("utf-8"), "entry.txt bytes differ from ENTRY"
    assert 1 <= len(raw.decode("utf-8")) <= 120, "entry length out of gate"


if __name__ == "__main__":
    main()
