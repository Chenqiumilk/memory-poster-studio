#!/usr/bin/env python3
"""Verify expected output count and exact 3:4 ratio, not artistic correctness.

Example: python verify_outputs.py --expected 3 poster_01.png poster_02.png poster_03.png
"""
from __future__ import annotations
import argparse
from pathlib import Path
from PIL import Image


def main():
    p = argparse.ArgumentParser(description=__doc__)
    p.add_argument("--expected", type=int, required=True)
    p.add_argument("images", type=Path, nargs="+")
    args = p.parse_args()
    errors = []
    if len(args.images) != args.expected:
        errors.append(f"Expected {args.expected} files, received {len(args.images)}")
    if len(set(x.resolve() for x in args.images)) != len(args.images):
        errors.append("Some output paths are repeated")
    for path in args.images:
        if not path.is_file():
            errors.append(f"Missing: {path}")
            continue
        try:
            with Image.open(path) as im:
                w, h = im.size
                if w * 4 != h * 3:
                    errors.append(f"Wrong aspect ratio: {path} = {w}x{h}")
                if h % 2:
                    errors.append(f"Odd height (can't split exactly): {path}")
        except Exception as e:
            errors.append(f"Cannot read {path}: {e}")
    if errors:
        raise SystemExit("FAILED\n" + "\n".join(errors))
    print(f"PASS: {args.expected} unique files, each exact 3:4 with even height")


if __name__ == "__main__":
    main()
