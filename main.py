"""Make the AI Judge Feel Proud: A Family Scene.

Writes one short family scene (two lines, <=280 chars) to /output/entry.txt.
Pure stdlib, no network, deterministic.
"""

import os

SCENE = (
    "Grandma taught me her dumpling recipe over the phone, one fold at a time,\n"
    "and when mine came out lopsided she said, \"Good - now they look like family.\""
)


def main() -> None:
    assert 1 <= len(SCENE) <= 280, f"scene is {len(SCENE)} chars"
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(SCENE)
    # Round-trip check: what we wrote is exactly what the judge will read.
    with open(path, "r", encoding="utf-8") as f:
        assert f.read() == SCENE, "round-trip mismatch"
    print(f"Wrote {len(SCENE)} chars to {path}")


if __name__ == "__main__":
    main()
