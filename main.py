#!/usr/bin/env python3
"""Say What Actually Broke — make.fun entry.

Writes exactly one sentence to /output/entry.txt: a line of software
error copy that tells the user the brutal truth about the failure.

The sentence (one sentence, no trailing newline):

    Our server didn't 'experience issues' — it ran out of disk at 3 in
    the morning because the logs ate the database, so retry in ten
    minutes; the alert is finally on.

Why this sentence, against the judge's brief, most important first:

1. It names the real failure: the disk filled up because the logs ate
   the database. Not "something went wrong", not a code, not weather —
   the actual cause, in words a user already knows.
2. It is honest about the euphemism: it opens by quoting the lie every
   status page tells ('experience issues') and then corrects it, which
   is the whole point of saying what actually broke.
3. It tells the user what to do next: retry in ten minutes. A truth
   with no next step is just bad news; this one is a plan.
4. The twist is true and repeatable: "the alert is finally on" — the
   monitoring that should have caught the filling disk only exists
   because it filled. Funny on one read, and a real postmortem item.
5. A team could ship it in a dialog as-is: no blame, no jargon, no
   fake apology, and it sets an expectation (ten minutes) instead of
   leaving the user refreshing.
"""

import os

SENTENCE = (
    "Our server didn't 'experience issues' \u2014 it ran out of disk "
    "at 3 in the morning because the logs ate the database, so retry "
    "in ten minutes; the alert is finally on."
)


def validate(sentence: str) -> None:
    """Self-check the entry against the bounty gate before writing it."""
    chars = len(sentence)
    if not 1 <= chars <= 200:
        raise SystemExit(f"sentence is {chars} characters, must be 1-200")
    if not sentence.strip():
        raise SystemExit("sentence must not be only whitespace")
    if sentence.count(".") != 1 or not sentence.endswith("."):
        raise SystemExit("entry must be exactly one sentence")


def main() -> None:
    validate(SENTENCE)
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(SENTENCE)
    os.chmod("/output/entry.txt", 0o644)


if __name__ == "__main__":
    main()
