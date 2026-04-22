import os

os.environ.setdefault("QT_QPA_PLATFORM", "offscreen")

from PySide6.QtWidgets import QApplication
from PySide6.QtGui import QAction

from qt_app.controller import Controller
from qt_app.window import MainWindow


def test_controller_is_singleton():
    assert Controller() is Controller()


def test_main_window_populates_actions_menu():
    app = QApplication.instance() or QApplication([])
    window = MainWindow()

    controller_action_texts = [action.text() for action in Controller().actions()]
    menu_action_texts = [action.text() for action in window.ui.menuActions.actions()]

    assert window.centralWidget() is window.ui.centralwidget
    assert menu_action_texts == controller_action_texts

    window.close()
    app.quit()


def test_controller_add_action_updates_menu():
    app = QApplication.instance() or QApplication([])
    controller = Controller()
    window = MainWindow()
    action = QAction("&External Action")

    controller.add_action(action)

    assert action in controller.actions()
    assert action in window.ui.menuActions.actions()

    controller.remove_action(action)

    assert action not in controller.actions()
    assert action not in window.ui.menuActions.actions()

    window.close()
    app.quit()
