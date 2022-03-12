import numpy as np
import matplotlib.pyplot as plt

"""
    Experimento: lançamento de duas moedas não viciadas
    Espaço amostral: S = {HH, HT, TH, TT}
    Evento: A = {Ambas saírem cara} = {HH} => Coin1 == H and Coin2 == H
            B = {Ao menos uma H} = {HH, HT, TH} => Coin1 == H or Coin2 == H
"""


def coin_flip(experiment: str) -> int:
    global condition
    coin1 = ["H", "T"]
    coin2 = ["H", "T"]

    coin1_flip = np.random.choice(coin1)
    coin2_flip = np.random.choice(coin2)

    if experiment == "A":
        condition = coin1_flip == "H" and coin2_flip == "H"
    if experiment == "B":
        condition = coin1_flip == "H" or coin2_flip == "H"

    if condition:
        return 1
    else:
        return 0


def graph(_real_value: float,
          _n_runs: int,
          _runs: list,
          _probs: list) -> None:
    plt.hlines(_real_value, 0, _n_runs, colors="brown", label="Valor Exato")
    plt.plot(_runs, _probs, label="Resultados")
    plt.xlabel("# Lançamentos")
    plt.ylabel("Probabilidades")
    plt.legend()
    plt.show()


if __name__ == '__main__':
    n_runs = 1000
    count = 0
    real_value = 1 / 4
    probs = []
    runs = []
    experiment = "A"

    for run in range(n_runs):
        count += coin_flip(experiment)
        probs.append(count / (run + 1))
        runs.append(run + 1)

    graph(real_value, n_runs, runs, probs)
