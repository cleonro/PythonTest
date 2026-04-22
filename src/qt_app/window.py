from PySide6.QtWidgets import QMainWindow, QMessageBox

from .controller import Controller
from .ui_window import Ui_MainWindow
 

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        # Load UI created in Qt Designer (window.ui -> ui_window.py)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        # initial status
        self.statusBar().showMessage("Ready")

        self.controller = Controller()
        self.controller.action_added.connect(self._add_controller_action)
        self.controller.action_removed.connect(self._remove_controller_action)
        for action in self.controller.actions():
            self._add_controller_action(action)

        # wire up signals
        self.ui.actionExit.triggered.connect(self.close)
        self.ui.actionAbout.triggered.connect(self.show_about)
        
        # show actions from tests_collection
        from . import tests_collection

    def show_about(self):
        QMessageBox.about(self, "About", "Qt App Skeleton\nUsing PySide6")

    def _add_controller_action(self, action):
        if action not in self.ui.menuActions.actions():
            self.ui.menuActions.addAction(action)

    def _remove_controller_action(self, action):
        self.ui.menuActions.removeAction(action)
