import numpy as np
import matplotlib.pyplot as plt


class NaiveLinearRegression:
    """
    Class for a naive implementation of linear regression
    """
    def __init__(self, n_points: int, parameter: float):
        self.error_msg = "to be implemented"
        self.n_points = n_points
        self.parameter = parameter

    @staticmethod
    def hat_matrix(self):
        return AssertionError(self.error_msg)

    @staticmethod
    def parameters_calc(self):
        return AssertionError(self.error_msg)

    def synthetic_data(self):
        _x = np.random.rand(self.n_points)
        _noise = np.random.rand(self.n_points)
        _y = self.parameter * _x + _noise

        return _x, _y


if __name__=='__main__':
    x, y = NaiveLinearRegression(50, 1.2).synthetic_data()

    plt.scatter(x, y)
    plt.show()
