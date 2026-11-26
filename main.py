"""Write the 3AM commit message entry to entry.txt.

Standard library only. Writes exactly one line, no trailing newline.
"""

import os

LINE = "fix: the tests pass. i have run them once. i will not run them again. goodnight."

MAX_CHARS = 139


def main() -> None:
    if not 1 <= len(LINE) <= MAX_CHARS or not LINE.strip():
        raise ValueError(f"entry line must be 1-{MAX_CHARS} chars, got {len(LINE)}")
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(LINE)


if __name__ == "__main__":
    main()
