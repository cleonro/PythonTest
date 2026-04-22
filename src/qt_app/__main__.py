"""Module entrypoint for `python -m qt_app`"""

from .main import main as start_main


def main_entry():
    return start_main()

def main():
    # Keep a simple wrapper so the console_scripts in pyproject works
    return main_entry()


if __name__ == "__main__":
    raise SystemExit(main())
