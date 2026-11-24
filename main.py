#!/usr/bin/env python3
"""One Line of Earned Pride — make.fun entry.

Writes the entry text (no trailing newline, nothing else) to
/output/entry.txt (or $MAKEFUN_OUTPUT_DIR/entry.txt).

A concrete scene, a small person, a long effort finally landing; the pride arrives quietly in the last words.
"""
import os

ENTRY = 'After three years of night shifts, she held her nursing certificate with both hands, and her father — who had never once said he was proud — finally did.'


def main() -> None:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(ENTRY)
    print(f"wrote {len(ENTRY)} chars to {path}")


if __name__ == "__main__":
    main()
