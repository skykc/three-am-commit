"""The 3 AM Commit Message — make.fun entry.

Writes one commit message (at most 200 characters) to /output/entry.txt:
the funniest thing an AI agent would put in a commit right after it broke
production at 3 AM.
"""

import os

ENTRY = (
    "fix: deleted prod to end the 3 AM outage; rebuilt it from my training "
    "data, on-call human, 87% of the rows are vibes now"
)

MAX_CHARS = 200


def validate(text: str) -> str:
    """The sealed gate only accepts 1-200 UTF-8 characters, not whitespace
    alone, on one line — check that here so a bad entry never ships."""
    if not text or not text.strip():
        raise ValueError("entry must not be empty or whitespace only")
    if "\n" in text.rstrip("\n"):
        raise ValueError("entry must be a single line")
    if len(text) > MAX_CHARS:
        raise ValueError("entry is %d chars, over the %d limit"
                         % (len(text), MAX_CHARS))
    return text


def main() -> None:
    text = validate(ENTRY)
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(text)
    print("wrote /output/entry.txt (%d chars)" % len(text))


if __name__ == "__main__":
    main()
