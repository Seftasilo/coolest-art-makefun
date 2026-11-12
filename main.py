#!/usr/bin/env python3
"""Coolest art entry (make.fun coolest-art-01).

The art is the entry.png bundled beside this file: "Stardust Whale", a
colossal whale made of stars and nebula light swimming over a lantern-lit
coastal town, with a small boy on a rooftop reaching toward it.

This program copies those exact bytes to /output/entry.png. It uses only
the Python standard library, touches no network, reads no clock, and
writes the same bytes on every run, so two runs are byte-identical.
"""

import os
import sys


def main() -> int:
    here = os.path.dirname(os.path.abspath(__file__))
    source = os.path.join(here, "entry.png")
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    target = os.path.join(out_dir, "entry.png")

    with open(source, "rb") as f:
        data = f.read()

    os.makedirs(out_dir, exist_ok=True)
    with open(target, "wb") as f:
        f.write(data)

    # Confirm the copy is complete: the gate scores the exact bytes written.
    written = os.path.getsize(target)
    if written != len(data):
        print(f"entry.png: wrote {written} of {len(data)} bytes",
              file=sys.stderr)
        return 1
    print(f"entry.png: {written} bytes -> {target}", file=sys.stderr)
    return 0


if __name__ == "__main__":
    sys.exit(main())
