import numpy as np
import matplotlib.pyplot as plt


class NaiveLinearRegression:
    """
    Class for a naive implementation of linear regression
    """
    def __init__(self, n_points: int, coefficient: float) -> None:
        self.error_msg = "to be implemented"
        self.n_points = n_points
        self.coefficient = coefficient

    @staticmethod
    def hat_matrix(self):
        return AssertionError(self.error_msg)

    @staticmethod
    def parameters_calc(self):
        """ Function responsible for calculate the model parameter
        :arg:
            - _x (list) input data
            - hat_matrix (list)

        :returns:
            - (float) fitting parameter"""
        return np.dot(self._x, self.hat_matrix)

    def synthetic_data(self) -> list:
        """ Function responsible for create the synthetic.
        :arg:
            - n_points (int) number of points in each axis
            - coefficient (float) coefficient used to construct _y from _x

        :returns:
            - x, y (list) two lists containing the synthetic data
        """
        _x = np.random.rand(self.n_points)
        _noise = np.random.rand(self.n_points)
        _y = self.coefficient * _x + _noise

        return _x, _y


if __name__ == '__main__':
    x, y = NaiveLinearRegression(50, 1.2).synthetic_data()

    plt.scatter(x, y)
    plt.show()
