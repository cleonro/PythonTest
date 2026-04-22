from PySide6.QtWidgets import QApplication
import sys

from .window import MainWindow


def main(argv=None):
    argv = argv if argv is not None else sys.argv
    app = QApplication(argv)
    window = MainWindow()
    window.show()
    return app.exec()


if __name__ == "__main__":
    raise SystemExit(main())
