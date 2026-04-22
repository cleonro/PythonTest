# Qt App Skeleton ✅

Minimal Python Qt application scaffold using PySide6.

## What's included

- A small package in `src/qt_app` with a `MainWindow` and a `main()` entrypoint
- `pyproject.toml` with an installable `qt-app` script
- `requirements.txt` with `PySide6`

## Quick start

1. Create and activate a venv

```bash
python -m venv .venv
source .venv/bin/activate
```

2. Install dependencies

```bash
pip install -r requirements.txt
# or install package in editable mode
pip install -e .
```

3. Run the app

```bash
python -m qt_app
# or (after installing) run
qt-app
```

## Notes

- Uses **PySide6** by default; you can switch to PyQt6 if you prefer.
- UI: the project includes `src/qt_app/window.ui` (created with Qt Designer). The generated `src/qt_app/ui_window.py` is used by `MainWindow`.

  To regenerate the Python UI file from the `.ui` file run:

  ```bash
  # after activating venv and installing requirements
  pyside6-uic src/qt_app/window.ui -o src/qt_app/ui_window.py
  # or use the helper script
  ./scripts/gen_ui.sh
  ```

- This is a skeleton—feel free to request additional features (tray icon, preferences, docs, CI, packaging)!
