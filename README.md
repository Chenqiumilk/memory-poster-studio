# Memory Poster Studio

Turn each uploaded photo into a standalone 3:4 illustrated memory poster.

## Output Rules

1. Create one poster for every input photo. Never combine photos. Never skip an input.
2. Split each poster into equal halves. Keep the source photo above the hand-drawn memory panel.
3. Preserve the subject, pose, clothing, light and colors. Do not regenerate faces.
4. Select six distinct details visible in the photo. Use a loose grid with three columns and two rows.
5. If fewer than six distinct details exist, select exactly three. Do not invent details to fill the layout.
6. Use naïve doodles, crayon grain, colored pencil marks, warm paper and short handwritten captions.
7. Deliver each poster separately. Confirm that the output count matches the input count.

## Usage

Install this folder as a skill in a compatible assistant with image generation support. Upload photos and request:

> Create a Memory Poster Studio poster for every uploaded photo. Preserve each source photo in the upper half. Draw six distinct memory details when available. Draw three if fewer than six exist. Return one finished poster per input photo.

## Local Composition

Generate the illustrated lower panel with an image model. Then compose the poster with Pillow.

```bash
python -m pip install Pillow
python scripts/compose_poster.py --photo photo.jpg --doodles doodles.png --output poster.png
python scripts/verify_outputs.py --expected 1 poster.png
```

The composition script fits the original photo without stretching the subject. The verification script checks file count and image ratio. Visual accuracy still requires review.

See [`SKILL.md`](SKILL.md) for the complete generation rules.
