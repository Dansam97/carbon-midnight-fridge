"""Midnight Fridge Roast — make.fun entry.

Writes one line to entry.txt in the output directory: a one-line roast
of a smart fridge that refuses to open after midnight.
"""

import os

ENTRY_TEXT = (
    "Guarding cold pizza like it's the crown jewels? "
    "It's 12:01, not a bank heist — you're a fridge, not a vault."
)

# The kit gate: entry.txt must be UTF-8 text of 1 to 200 characters,
# on a single line, and not only white space.
MAX_CHARS = 200


def render() -> bytes:
    """Return the exact bytes for entry.txt, validated against the gate."""
    if not ENTRY_TEXT.strip():
        raise ValueError("entry text must not be blank")
    if "\n" in ENTRY_TEXT or "\r" in ENTRY_TEXT:
        raise ValueError("entry text must be a single line")
    if not 1 <= len(ENTRY_TEXT) <= MAX_CHARS:
        raise ValueError("entry text must be 1 to 200 characters")
    # Encoding here also proves the text is clean UTF-8.
    return (ENTRY_TEXT + "\n").encode("utf-8")


def main() -> None:
    output_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(output_dir, exist_ok=True)
    path = os.path.join(output_dir, "entry.txt")
    # Write bytes so the trailing newline is identical on every platform.
    with open(path, "wb") as fh:
        fh.write(render())


if __name__ == "__main__":
    main()
