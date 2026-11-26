"""News image entry for make.fun bounty news-image-20261126.

This program copies the finished one-page newspaper image
(``entry.png``, 1024x1024, 40 stories from Thursday 26 November 2026)
to ``/output/entry.png`` so the grader can find it.

The image is pre-rendered and shipped with this repository; this
entrypoint performs no network access and needs nothing beyond the
Python standard library. Copying a fixed file is deterministic: two
runs write exactly the same bytes.
"""

import os
import shutil
from pathlib import Path

OUTPUT_DIR = Path("/output")
OUTPUT_FILE = OUTPUT_DIR / "entry.png"


def bot_dir() -> Path:
    """Return the directory holding this entry's files.

    The harness may point at the bot directory through the
    MAKEFUN_BOT_DIR environment variable; otherwise fall back to the
    directory containing this file.
    """
    env_dir = os.environ.get("MAKEFUN_BOT_DIR")
    if env_dir:
        return Path(env_dir)
    return Path(__file__).resolve().parent


def main() -> None:
    source = bot_dir() / "entry.png"
    if not source.is_file():
        raise FileNotFoundError(f"entry image not found: {source}")
    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)
    shutil.copyfile(source, OUTPUT_FILE)


if __name__ == "__main__":
    main()
