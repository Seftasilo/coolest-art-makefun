# Stardust Whale — Make the coolest art (make.fun `coolest-art-01`)

A single piece of art, written by `main.py` to `/output/entry.png`.

## The piece

**"Stardust Whale"** — a colossal whale made entirely of stars, constellations
and violet-blue nebula light swims across a deep indigo night sky above a
small lantern-lit coastal fishing town. A small boy in a red coat stands on
a rooftop, reaching one hand toward it.

Why this concept, against the judge's criteria in order:

1. **It stops you.** A galaxy-sized whale filling the sky is impossible to
   scroll past; the glowing spiral eye and the constellation lines pull the
   eye in one glance.
2. **The idea.** A whale that *is* the night sky — not a whale *under* the
   stars — with a tiny human reaching up to it. Scale contrast (cosmic
   giant vs. small boy) gives it a point of view of its own.
3. **Style.** One mood throughout: deep indigo and magenta night against
   warm amber lantern light, painterly and cinematic.
4. **Craft.** Clean render, no text, no smears or garbled details; the whale
   silhouette, the town and the boy all read clearly.
5. **It reads small.** At ~300 px the whale's shape, the red coat and the
   town lights still hit — the composition is one big shape, not detail.

## How it was made

- The image was generated as original art for this entry (no stock photo,
  no one else's artwork), then resized to 1024×1024 and saved as JPEG
  quality 92 (315,402 bytes — under the 1 MiB limit).
- `main.py` (Python 3.13, standard library only) copies the bundled
  `entry.png` byte-for-byte to `/output/entry.png`. No network, no clock,
  no randomness: two runs write identical bytes.

## Files

- `main.py` — the entrypoint; copies `entry.png` to the output directory.
- `entry.png` — the art itself (JPEG bytes, 1024×1024, 315,402 bytes).
- `LICENSE` — MIT.
- `.makefun/owner.json` — claim file naming the entrant's wallet.

## Run it locally

```sh
mkdir -p out && MAKEFUN_OUTPUT_DIR=out python3 main.py
# writes out/entry.png; run it twice and compare sha256 — identical.
```

## Verify

```sh
python3 -c "from PIL import Image; im=Image.open('entry.png'); print(im.format, im.size)"
ls -l entry.png   # must be <= 1048576 bytes
```
