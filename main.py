"""The Dog Ate My Homework: Funniest Excuse — make.fun entry.

Writes one line to /output/entry.txt: the excuse a dog gives after
being caught eating the homework. The dog does not deny it, he
reframes it as quality control: he only taste-tested the essay, and
frankly the volcano piece needed more flavor and fewer facts.
"""

import os

ENTRY = (
    "I did not eat your homework, I taste-tested it, and frankly the "
    "essay on volcanoes needed more flavor, fewer facts, and a better "
    "title."
)

MAX_CHARS = 200


def main() -> None:
    text = ENTRY
    assert text.strip(), "entry must not be only whitespace"
    assert len(text) <= MAX_CHARS, (
        f"entry is {len(text)} characters, over the {MAX_CHARS} limit"
    )
    out_dir = os.environ.get("ENTRY_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    # Written byte-for-byte with no trailing newline, so the file holds
    # exactly len(ENTRY) characters and nothing else.
    with open(path, "w", encoding="utf-8") as handle:
        handle.write(text)
    with open(path, "r", encoding="utf-8") as handle:
        assert handle.read() == text, "entry.txt does not match ENTRY"


if __name__ == "__main__":
    main()
