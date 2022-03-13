import numpy as np
import matplotlib.pyplot as plt
plt.style.use('ggplot')
from numpy import ndarray


class NaiveLinearRegression:
    """
    Class for a naive implementation of linear regression
    """

    def __init__(self, n_points: int, coefficient: float) -> None:
        self.error_msg = "to be implemented"
        self.n_points = n_points
        self.coefficient = coefficient

    @staticmethod
    def hat_matrix(_x: ndarray) -> ndarray:
        _determinant = np.dot(_x.T, _x)
        return _x.T / _determinant

    @staticmethod
    def parameters_calc(_x: ndarray,
                        hat_matrix: ndarray) -> float:
        """ Function responsible for calculate the model parameter
        :arg:
            - _x (list) input data
            - hat_matrix (list)

        :returns:
            - (float) fitting parameter"""
        return np.dot(_x, hat_matrix)

    def synthetic_data(self) -> tuple:
        """ Function responsible for create the synthetic.
        :arg:
            - n_points (int) number of points in each axis
            - coefficient (float) coefficient used to construct _y from _x

        :returns:
            - x, y (list) two lists containing the synthetic data
        """
        _noise = np.array([np.random.randn() for _ in range(self.n_points)])
        _x = np.array([np.random.randn() for _ in range(self.n_points)])
        _y = self.coefficient * _x + _noise

        return _x, _y


if __name__ == '__main__':
    # Inicialização dos parâmetros da simulação
    N = 5000
    coefficient = 1.2
     # Construção do modelo a partir da classa acima
    regression = NaiveLinearRegression(N, coefficient)

    # Geração dos dados sintéticos
    x, y = regression.synthetic_data()

    # Cálculo da matriz chapeu
    hat_matrix = regression.hat_matrix(x)

    # Ajuste dos parâmetros
    beta = regression.parameters_calc(y, hat_matrix)
    print(beta)

    adjustment = beta * x


    # Construção de um gráfico para visualização dos resultados
    plt.scatter(x, y, color="blue", alpha=0.1, label="Synthetic Data")
    plt.plot(x, adjustment, color="brown", linewidth=0.8, label="Adjusted Model")
    plt.legend()
    plt.grid(True)
    plt.xlabel("X1")
    plt.ylabel("Y")
    plt.show()
