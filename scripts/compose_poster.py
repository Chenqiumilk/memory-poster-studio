#!/usr/bin/env python3
"""Compose a 3:4 poster from an original photo and a doodle-only panel.

This retains all foreground pixels of the *original* photo, rather than
rendering a fresh interpretation of the person or pet.

Example:
 python compose_poster.py --photo photo.jpg --doodles doodles.png \\
   --output poster.png --width 1200 --height 1600
"""
from __future__ import annotations
import argparse
from pathlib import Path
from PIL import Image, ImageFilter, ImageOps


def fit_with_protected_subject(image: Image.Image, size: tuple[int, int]) -> Image.Image:
    """Fit full source image without stretching or cropping; softly extend margins."""
    w, h = size
    original = ImageOps.exif_transpose(image).convert("RGB")
    # Soft background uses source colors; original remains pixel-faithfully visible.
    background = ImageOps.fit(original, size, method=Image.Resampling.LANCZOS)
    background = background.filter(ImageFilter.GaussianBlur(radius=max(12, w // 35)))
    # Dim blurred side bars slightly to distinguish the preserved image gently.
    background = Image.blend(background, Image.new("RGB", size, (248, 244, 237)), 0.15)
    foreground = ImageOps.contain(original, size, method=Image.Resampling.LANCZOS)
    left = (w - foreground.width) // 2
    top = (h - foreground.height) // 2
    background.paste(foreground, (left, top))
    return background


def compose(photo: Path, doodles: Path, output: Path, width: int, height: int) -> None:
    if width * 4 != height * 3:
        raise ValueError("Output must be exactly 3:4 (width:height)")
    if height % 2:
        raise ValueError("Height must be even for exact 50:50 split")
    half = height // 2
    with Image.open(photo) as photo_img, Image.open(doodles) as doodle_img:
        top = fit_with_protected_subject(photo_img, (width, half))
        # The supplied doodle must depict only the lower half, not a whole poster.
        bottom = ImageOps.fit(ImageOps.exif_transpose(doodle_img).convert("RGB"),
                              (width, half), method=Image.Resampling.LANCZOS)
        poster = Image.new("RGB", (width, height))
        poster.paste(top, (0, 0))
        poster.paste(bottom, (0, half))
        output.parent.mkdir(parents=True, exist_ok=True)
        if output.suffix.lower() in (".jpg", ".jpeg"):
            poster.save(output, quality=95, subsampling=0)
        else:
            poster.save(output)
    print(f"Created: {output} ({width}x{height}; split y={half})")


def main():
    p = argparse.ArgumentParser(description=__doc__)
    p.add_argument("--photo", type=Path, required=True)
    p.add_argument("--doodles", type=Path, required=True, help="Doodle-only image, no source photo")
    p.add_argument("--output", type=Path, required=True)
    p.add_argument("--width", type=int, default=1200)
    p.add_argument("--height", type=int, default=1600)
    args = p.parse_args()
    compose(args.photo, args.doodles, args.output, args.width, args.height)


if __name__ == "__main__":
    main()
