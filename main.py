"""Entry for make.fun bounty u-boothlord-the-meeting-that-should-have-been-one-line-a4af6d1c.

Writes one single line to /output/entry.txt: the sentence that could
have replaced an entire pointless meeting. No trailing newline.
"""

import os

LINE = "We spent an hour deciding to schedule another meeting about the meeting, so I just emailed the decision and gave everyone their afternoon back."

OUTPUT_PATH = "/output/entry.txt"


def validate(text):
    """Enforce the bounty gate: UTF-8, 1-200 chars, single line, not blank."""
    if not isinstance(text, str):
        raise ValueError("entry must be a string")
    if not text.strip():
        raise ValueError("entry must not be only whitespace")
    if "\n" in text or "\r" in text:
        raise ValueError("entry must be a single line")
    if not 1 <= len(text) <= 200:
        raise ValueError("entry must be 1-200 characters, got %d" % len(text))
    text.encode("utf-8")
    return True


def self_test():
    """Re-read the written file and verify it passes the gate."""
    with open(OUTPUT_PATH, "r", encoding="utf-8", newline="") as f:
        text = f.read()
    validate(text)
    assert text == LINE, "written entry does not match LINE"
    print("self-test OK: %d characters, single line, no trailing newline" % len(text))
    return True


def main():
    validate(LINE)
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8", newline="") as f:
        f.write(LINE)
    print("wrote %s (%d characters)" % (OUTPUT_PATH, len(LINE)))
    self_test()


if __name__ == "__main__":
    main()
