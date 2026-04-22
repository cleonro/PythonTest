#!/usr/bin/env bash
# Generate ui_window.py from the Designer .ui file
set -euo pipefail
UI_FILE="src/qt_app/window.ui"
OUT_FILE="src/qt_app/ui_window.py"

if ! command -v pyside6-uic >/dev/null 2>&1; then
  echo "pyside6-uic not found. Install PySide6 or use 'pip install -r requirements.txt'"
  exit 1
fi

pyside6-uic "$UI_FILE" -o "$OUT_FILE"

echo "Generated $OUT_FILE from $UI_FILE"
