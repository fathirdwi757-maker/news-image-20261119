#!/usr/bin/env python3
"""News-image entry for 19 November 2026 (make.fun, Python 3.13, stdlib only).

The infographic lives in this repository as ``entry.png`` beside this file.
The program copies it, byte for byte, to the grader's output location:

* ``$MAKEFUN_OUTPUT_DIR/entry.png`` when that variable is set,
* otherwise ``/output/entry.png``,
* with ``./output/entry.png`` as a last-resort fallback when ``/output``
  cannot be created or written.

No network, no third-party packages, no randomness: two runs on the same
repository always write identical bytes.
"""

import os
import shutil
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
SOURCE = os.path.join(HERE, "entry.png")


def output_dir():
    """Resolve where entry.png must be written, in priority order."""
    from_env = os.environ.get("MAKEFUN_OUTPUT_DIR")
    if from_env:
        return from_env
    return "/output"


def main():
    """Copy the repository's entry.png to the resolved output directory."""
    target_dir = output_dir()
    try:
        os.makedirs(target_dir, exist_ok=True)
    except OSError:
        if os.environ.get("MAKEFUN_OUTPUT_DIR"):
            raise
        target_dir = os.path.join(os.getcwd(), "output")
        os.makedirs(target_dir, exist_ok=True)
    target = os.path.join(target_dir, "entry.png")
    try:
        shutil.copyfile(SOURCE, target)
    except OSError:
        if os.environ.get("MAKEFUN_OUTPUT_DIR") or target_dir != "/output":
            raise
        target_dir = os.path.join(os.getcwd(), "output")
        os.makedirs(target_dir, exist_ok=True)
        target = os.path.join(target_dir, "entry.png")
        shutil.copyfile(SOURCE, target)
    print("wrote", target)
    return 0


if __name__ == "__main__":
    sys.exit(main())
