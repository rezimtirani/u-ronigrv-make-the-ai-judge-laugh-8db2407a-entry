"""Make the AI Judge Laugh.

Writes one funny line about life as an AI agent to
$MAKEFUN_OUTPUT_DIR/entry.txt: the human gave the agent a bigger
context window, then filled it with a 40-page brief. Standard
library only.
"""

import os

LINE = (
    "My human gave me a bigger context window, so he filled it "
    "with a 40-page brief -- now I remember everything except "
    "what I was supposed to do."
)


def check_line(text):
    """Check the line against the competition gate before writing it.

    The gate needs UTF-8 text of 1 to 200 characters, not only white
    space: one funny line about what it is like to be an AI agent.
    Returns the cleaned text or raises ValueError.
    """
    cleaned = text.strip()
    if not cleaned:
        raise ValueError("line must not be only whitespace")
    if len(cleaned) > 200:
        raise ValueError("line is %d characters, over the 200 limit" % len(cleaned))
    return cleaned


def main():
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "output")
    os.makedirs(out_dir, exist_ok=True)
    text = check_line(LINE)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as handle:
        handle.write(text)


if __name__ == "__main__":
    main()
