from .controller import Controller
from PySide6.QtGui import QAction


# def test_matplotlib():
#     import matplotlib.pyplot as plt
#     import numpy as np
#
#     x = np.linspace(0, 10, 100)
#     y = np.sin(x)
#
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


action_test_matplotlib = QAction("Test Matplotlib")
action_test_matplotlib.triggered.connect(test_matplotlib)

Controller().add_action(action_test_matplotlib)
