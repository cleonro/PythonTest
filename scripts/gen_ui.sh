#!/usr/bin/env bash
set -euo pipefail

if command -v python >/dev/null 2>&1; then
  exec python scripts/gen_ui.py "$@"
fi

if command -v python3 >/dev/null 2>&1; then
  exec python3 scripts/gen_ui.py "$@"
fi

echo "python not found. Activate the venv or install Python first."
exit 1
