from PySide6.QtCore import QObject, Signal, Slot
from PySide6.QtGui import QAction
from PySide6.QtWidgets import QApplication, QMainWindow, QMessageBox


class Controller(QObject):
    action_added = Signal(object)
    action_removed = Signal(object)
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance

    def __init__(self):
        if getattr(self, "_initialized", False):
            return

        super().__init__()
        self._initialized = True
        self._actions = []
        self._build_actions()

    def actions(self):
        return tuple(self._actions)

    def add_action(self, action):
        if not isinstance(action, QAction):
            raise TypeError("action must be a QAction instance")

        if action not in self._actions:
            if action.parent() is None:
                action.setParent(self)
            self._actions.append(action)
            self.action_added.emit(action)

        return action

    def remove_action(self, action):
        if action in self._actions:
            self._actions.remove(action)
            self.action_removed.emit(action)

    def _build_actions(self):
        say_hello_action = QAction("&Say Hello", self)
        say_hello_action.setStatusTip("Show a greeting dialog")
        say_hello_action.triggered.connect(self.say_hello)

        plot_demo_action = QAction("&Plot Demo", self)
        plot_demo_action.setStatusTip("Open the sample matplotlib plot")
        plot_demo_action.triggered.connect(self.plot_demo)

        self.add_action(say_hello_action)
        self.add_action(plot_demo_action)

    def _main_window(self):
        window = QApplication.activeWindow()
        if isinstance(window, QMainWindow):
            return window
        return None

    @Slot()
    def say_hello(self):
        window = self._main_window()
        if window is not None:
            window.statusBar().showMessage("Hello from the controller")
        QMessageBox.information(window, "Hello", "Hello from the Actions menu")

    @Slot()
    def plot_demo(self):
        window = self._main_window()
        if window is not None:
            window.statusBar().showMessage("Opening plot demo")
        self._show_plot()

    def _show_plot(self):
        import matplotlib.pyplot as plt
        import numpy

        x = numpy.random.normal(5.0, 3.0, 100000)
        y = numpy.sin(x)
        plt.plot(x, y)
        plt.show()
