from PySide6.QtWidgets import QMainWindow, QMessageBox
from PySide6.QtCore import Slot

from .ui_window import Ui_MainWindow

# def test_matplotlib():
#     import matplotlib.pyplot as plt
#     import numpy as np

#     x = np.linspace(0, 10, 100)
#     y = np.sin(x)

#     plt.plot(x, y)
#     plt.title("Sine Wave")
#     plt.xlabel("x")
#     plt.ylabel("sin(x)")
#     plt.grid()
#     plt.show()

def test_matplotlib():
    import sys
    import matplotlib
    # matplotlib.use('Agg')

    import numpy
    import matplotlib.pyplot as plt

    x = numpy.random.normal(5.0, 3.0, 100000)
    y = numpy.sin(x)
    # plt.hist(x, 100)
    plt.plot(x, y)
    plt.show()


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        # Load UI created in Qt Designer (window.ui -> ui_window.py)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        # initial status
        self.statusBar().showMessage("Ready")

        # wire up signals
        self.ui.pushButton.clicked.connect(self.on_click)
        self.ui.actionExit.triggered.connect(self.close)
        self.ui.actionAbout.triggered.connect(self.show_about)

    @Slot()
    def on_click(self):
        self.statusBar().showMessage("Button clicked")
        QMessageBox.information(self, "Hello", "Button clicked!")

    def show_about(self):
        QMessageBox.about(self, "About", "Qt App Skeleton\nUsing PySide6")
