import numpy as np


def func_step(z: float) -> float:
    """Calcula a step function de uma constante

    Args:
        z (float): constate

    Returns:
        float: valor de step(z)
    """
    if z > 0:
        return 1
    else:
        return 0


def perceptron(x: list, w: list) -> float:
    """Realiza uma passagem ao longo de um perceptron simples
    Caso particular em que b = 0
    Args:
        x (list): valores de entrada
        w (list): pesos

    Retunrs:
        float: step(x.w)
    """
    z = np.dot(x.T, w)
    return func_step(z)


if __name__ == "__main__":
    x = np.array([0.1, 1.1, 3.9, 0.3])
    w = np.array([-0.2, 0.01, -0.3, 0.05])
    print(f"{np.dot(x.T, w)}")
    output = perceptron(x, w)
    print(f"{output}")
