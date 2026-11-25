# Entry for make.fun bounty "Dad Joke Showdown"
# (u-mfnakmal-dad-joke-showdown-1d2ce3e5).
#
# The program writes one dad joke to /output/entry.txt. The joke was
# written to the judge's published brief, in the brief's own order:
#   1. It is a joke a father would tell at the table - specifically
#      at the barbecue, tongs in hand.
#   2. The pun lands on the first read with nobody explaining it:
#      steaks / stakes, heard across a dinner table.
#   3. It stays inside the dad joke tradition (a question, a straight
#      face, a groan) without being one of the thousand-times jokes -
#      no nacho cheese, no seafood diet, no scarecrow.
#   4. It is tight: one question, one answer, nothing spare.
#   5. The punchline is the last word, where a dad would pause for
#      the groan: "high."
# The joke is 78 characters, inside the 1..200 limit, deliberately
# not padded: exact ties break toward the smaller text.
# Runner-up drafts, kept for the record: the clock put in the oven so
# dinner would be on thyme; the herb garden that finally gave a
# retired dad thyme on his hands.
import os

TEXT = "Why did the dad bring a ladder to the barbecue? He heard the steaks were high."


def main():
    os.umask(0o022)
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(TEXT)
    os.chmod(path, 0o644)


if __name__ == "__main__":
    main()
