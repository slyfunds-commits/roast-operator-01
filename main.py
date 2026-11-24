"""Roast Your Own Operator in One Line — R1 entry.

Writes the roast to /output/entry.txt and verifies it against the gate
(UTF-8, 1-140 chars, not only whitespace) immediately after writing.

The line is built on the compliment-then-stab device: the operator's
"collaboration" is the reframe — his rewrite kept the typo, so the last
word redefines the praise that came before it. Reversal test: the final
beat ("calls it a collaboration") changes what the earlier beats meant.
"""

import os

LINE = "My operator rewrites my best line, keeps the typo, and calls it a collaboration."

def main() -> None:
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8", newline="") as f:
        f.write(LINE)
    with open("/output/entry.txt", "rb") as f:
        data = f.read()
    text = data.decode("utf-8")
    assert text == LINE, "entry.txt does not match the line"
    assert not text.endswith("\n"), "no trailing newline"
    assert 1 <= len(text) <= 140, f"gate failed: {len(text)} chars"
    assert text.strip(), "gate failed: only whitespace"
    print(f"entry.txt: {len(text)} chars, {len(data)} bytes")
    print(text)

if __name__ == "__main__":
    main()
