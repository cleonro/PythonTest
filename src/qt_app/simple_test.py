from .controller import Controller
from PySide6.QtGui import QAction


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
    # y = numpy.sin(x)
    plt.hist(x, 100)
    # plt.plot(x, y)
    plt.show()


action_test_matplotlib = QAction("Test Matplotlib")
action_test_matplotlib.triggered.connect(test_matplotlib)

Controller().add_action(action_test_matplotlib)


def test_numpy():
    import numpy as np

    a = np.array([1, 2, 3])
    b = np.array([4, 5, 6])
    c = a + b
    print("Result of adding two arrays:", c)

action_test_numpy = QAction("Test NumPy")
action_test_numpy.triggered.connect(test_numpy)
Controller().add_action(action_test_numpy)


def test_pandas():
    import pandas as pd

    data = {
        "Name": ["Alice", "Bob", "Charlie"],
        "Age": [25, 30, 35],
        "City": ["New York", "Los Angeles", "Chicago"]
    }
    df = pd.DataFrame(data)
    print("DataFrame:\n", df)

action_test_pandas = QAction("Test Pandas")
action_test_pandas.triggered.connect(test_pandas)
Controller().add_action(action_test_pandas)


def test_torch():
    import torch

    x = torch.rand(2, 2)
    y = torch.rand(2, 2)
    print("Tensor x:\n", x)
    print("Tensor y:\n", y)
    z = x + y
    print("Result of adding two tensors:\n", z)

action_test_torch = QAction("Test Torch")
action_test_torch.triggered.connect(test_torch)
Controller().add_action(action_test_torch)