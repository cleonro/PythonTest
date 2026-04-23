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
   

    def _main_window(self):
        window = QApplication.activeWindow()
        if isinstance(window, QMainWindow):
            return window
        return None

