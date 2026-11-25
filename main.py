"""Make the AI Judge Laugh — one office-life joke, one line, under 200 chars.

Writes the entry to /output/entry.txt (or $MAKEFUN_OUTPUT_DIR / $OUTPUT_DIR).
"""

import os

# Sealed gate: entry must be UTF-8 text of 1 to 200 characters.
# This line is 119 characters: well inside the gate, no padding needed.
MAX_CHARS = 200

ENTRY = (
    "My boss asked for a quick sync, so I synced my calendar, my inbox, "
    "and my will to live \u2014 all three are still buffering."
)


def main() -> None:
    assert 1 <= len(ENTRY) <= MAX_CHARS, f"entry is {len(ENTRY)} chars"
    assert "\n" not in ENTRY.strip(), "entry must be a single line"
    out_dir = (
        os.environ.get("MAKEFUN_OUTPUT_DIR")
        or os.environ.get("OUTPUT_DIR")
        or "/output"
    )
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(ENTRY)


if __name__ == "__main__":
    main()
