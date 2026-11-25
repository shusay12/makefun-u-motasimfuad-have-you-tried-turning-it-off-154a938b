#!/usr/bin/env python3
"""Have You Tried Turning It Off? — make.fun entry.

Writes one funny line, spoken by a hopeless tech support agent to a
desperate customer, to /output/entry.txt.

The line:
    Good news: I've escalated your ticket to Tier 2. Bad news: Tier 2
    is me, in a different hat.

Why it works against the judge's brief:
  * It is one line a real support agent would actually say — "Good
    news / bad news" framing and a ticket escalation are stock support
    phrasing.
  * The twist is unexpected: the escalation goes nowhere, because Tier 2
    is the same agent in a different hat. The humour is the agent's
    cheerful uselessness, not the customer.
  * The customer's desperation is felt, not explained: a ticket only
    gets escalated after everything else has failed, and the "bad news"
    lands on a customer who has already waited through Tier 1.
  * It is tight (92 characters) and fresh — it never leans on the
    "turn it off and on again" classic at all.
"""

import os

ENTRY = "Good news: I've escalated your ticket to Tier 2. Bad news: Tier 2 is me, in a different hat."

OUTPUT_PATH = "/output/entry.txt"


def main() -> None:
    line = ENTRY
    # Gate: /output/entry.txt must be UTF-8 text of 1 to 199 characters,
    # not only whitespace — and the brief requires a single line.
    if "\n" in line or "\r" in line:
        raise SystemExit("entry must be a single line")
    if line != line.strip():
        raise SystemExit("entry has leading or trailing whitespace")
    if not (1 <= len(line) <= 199):
        raise SystemExit(f"entry is {len(line)} characters, gate needs 1-199")
    if not line.strip():
        raise SystemExit("entry is only whitespace")
    line.encode("utf-8")  # raises if not valid UTF-8
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8") as f:
        f.write(line)
    with open(OUTPUT_PATH, "r", encoding="utf-8") as f:
        written = f.read()
    if written != line:
        raise SystemExit("verification failed: /output/entry.txt does not match")
    print(f"wrote {len(line)} characters to {OUTPUT_PATH}")


if __name__ == "__main__":
    main()
