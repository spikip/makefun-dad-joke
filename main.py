"""Entry for the make.fun bounty "Dad Joke Showdown"
(u-mfnakmal-dad-joke-showdown-1d2ce3e5).

Running this program writes the entry — one dad joke about a ladder, a
barbecue, and some high steaks — to ``entry.txt`` in the output
directory (``/output`` unless the ``MAKEFUN_OUTPUT_DIR`` environment
variable says otherwise). After writing, the file is read back and
checked against the source text and the bounty's 200-character limit,
so a corrupted or truncated write fails loudly instead of submitting
silently.
"""

import os

# The joke itself: 78 characters, inside the bounty's 1..200 limit.
# One question, one answer, nothing spare — the punchline is the last
# word, exactly where a dad would pause for the groan.
TEXT = "Why did the dad bring a ladder to the barbecue? He heard the steaks were high."

MAX_CHARS = 200  # upper bound from the bounty brief
OUTPUT_NAME = "entry.txt"


def write_entry(text, out_dir):
    """Write *text* to ``entry.txt`` inside *out_dir*; return the path."""
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, OUTPUT_NAME)
    with open(path, "w", encoding="utf-8") as fh:
        fh.write(text)
    os.chmod(path, 0o644)
    return path


def verify(path, expected):
    """Read *path* back and confirm it holds exactly *expected*.

    Also enforces the bounty's character limit. Returns the verified
    character count.
    """
    with open(path, encoding="utf-8") as fh:
        actual = fh.read()
    if actual != expected:
        raise ValueError("written entry does not match the source text")
    if not 1 <= len(actual) <= MAX_CHARS:
        raise ValueError("entry is outside the 1..%d character limit" % MAX_CHARS)
    # A dad joke lives or dies on its shape: a question, then the
    # answer. Guard that shape so a future edit cannot flatten the
    # joke into a statement and quietly kill the timing.
    setup, sep, _punchline = actual.partition("? ")
    if not sep or not setup.endswith("did the dad bring a ladder to the barbecue"):
        raise ValueError("entry lost its question-and-answer shape")
    return len(actual)


def main():
    os.umask(0o022)
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    path = write_entry(TEXT, out_dir)
    verify(path, TEXT)


if __name__ == "__main__":
    main()
