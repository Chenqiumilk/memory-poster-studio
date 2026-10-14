# Memory Poster Studio — Visual System

## Fixed composition

- Canvas: 3:4 portrait, e.g. 1200×1600 px (high-resolution variants at same aspect ratio allowed).
- Upper photo: y = 0 to 799 px (exactly 50% of total height). Lower doodle: y = 800 to 1599 px.
- Upper photo preserves the actual input person's/pet's face, posture, clothes, scene and lighting; no identity edits.
- Lower area: warm white natural paper (#F7F3EA as a loose reference, not a rigid brand token); paper-fiber or matte-grain texture; ample negative space.
- No thick dividing lines, graphic cards, rigid grid borders, black section outlines, or glossy gradients.

## Memory unit selection

Consider, in order: defining subject / meaningful interaction / identifiable object / distinctive outfit / motion gesture / place detail / weather-light / small concrete accessory. Prefer six distinct things to six variations of the same idea.

- >=6 **meaningfully distinct visible** candidates: choose exactly 6; 2 columns × 3 rows or 3 columns × 2 rows? **Always visually present as 3 columns × 2 rows**, regardless of the textual notation 2×3 (2 rows × 3 columns).
- <6 distinct candidates: choose exactly 3; one wide row of 3 with generous whitespace or a very light organic stagger.
- In particular 4 or 5 candidates still means exactly **3**, not 4/5 or fabricated six.
- Hand-lettered title and small doodle decorations do not count. If a composition includes a small ornamental heart, it should read as ornament, not a fourth or seventh item.

## Hand drawing

- Juvenile but intentional, like a private sketchbook or independent zine.
- Slightly shaky hand-ink outlines, occasional gap, variable pressure, no perfect geometry.
- Uneven sparse wax crayon, colored pencil, dry pigment, visible white paper between strokes.
- Flat/spot color, minimal shading, warm pastel: dusty pink, peach, butter yellow, sage, desaturated sky blue, muted lilac, plus very dark brown/black outlines.
- Vary icon scale/angle/position slightly; shared invisible alignment, not perfect digital symmetry.
- Keep each icon readable and separate; no complex realistic scene per icon.
- Writing: short and natural handwritten English. Examples: "Park Days", "Together", "Little Adventures", "That Pink Sky". No made-up dates or relationships.

## Quality targets

- Feels like one photo's memory inventory, not six random clip-art stickers.
- Calm and spacious, not overloaded with filler shapes.
- Respect original lighting: sunset photos lean pink/lavender; cozy home photos lean beige/amber; spring photos may lean light green.
- Text should be subordinate to visual elements; no illegible word clouds.

## Pairing with pixel-exact photo composites

If tooling permits generating the lower illustration *alone*, render it as a 3:2 landscape image with six or three memory units plus title/caption, then composite with the untouched source photo in the upper half using `scripts/compose_poster.py`. The composite requires the photo and doodle to be separately generated; the script does not generate doodles itself.
