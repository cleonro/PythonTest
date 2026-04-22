def test_ui_module_importable():
    from qt_app.ui_window import Ui_MainWindow

    ui = Ui_MainWindow()
    assert hasattr(ui, "setupUi")
