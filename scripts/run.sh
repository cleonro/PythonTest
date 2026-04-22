#!/usr/bin/env bash
# Simple helper to run the app from the project root
source .venv/bin/activate 2>/dev/null || true
python -m qt_app
