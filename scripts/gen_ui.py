#!/usr/bin/env python3
"""Generate Python modules for all Qt Designer .ui files under src/."""

from __future__ import annotations

import shutil
import subprocess
import sys
from pathlib import Path


def find_uic() -> str:
    python_paths = [Path(sys.executable).parent, Path(sys.executable).resolve().parent]
    for python_dir in python_paths:
        candidates = [
            python_dir / "pyside6-uic",
            python_dir / "pyside6-uic.exe",
        ]
        for candidate in candidates:
            if candidate.exists():
                return str(candidate)

    uic = shutil.which("pyside6-uic")
    if uic:
        return uic

    raise SystemExit(
        "pyside6-uic not found for the selected interpreter. "
        "Install PySide6 in the active environment first."
    )


def main() -> int:
    root = Path(__file__).resolve().parents[1]
    src_dir = root / "src"
    ui_files = sorted(src_dir.rglob("*.ui"))

    if not ui_files:
        print("No .ui files found under src/")
        return 0

    uic = find_uic()
    for ui_file in ui_files:
        out_file = ui_file.with_name(f"ui_{ui_file.stem}.py")
        subprocess.run([uic, str(ui_file), "-o", str(out_file)], check=True)
        print(f"Generated {out_file.relative_to(root)} from {ui_file.relative_to(root)}")

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
