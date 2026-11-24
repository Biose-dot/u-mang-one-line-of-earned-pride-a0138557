#!/usr/bin/env python3
"""Draft entry writer for the earned-pride bounty (v1)."""

import os

ENTRY = "After three years of night shifts, she finally hung her own nameplate on the clinic door, and stood there a moment just reading it, smiling like the whole tired world had finally said thank you."

def main():
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(ENTRY)

if __name__ == "__main__":
    main()
