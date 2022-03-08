import numpy as np
import matplotlib.pyplot as plt
"""
Exeperimento: lançamento de duas moedas não viciadas
A = {sair dois H}
"""

def flip_coins() -> None:
    coin1 = ["H", "T"]
    coin2 = ["H", "T"]

    coin_flip1 = np.random.choice(coin1)
    coin_flip2 = np.random.choice(coin2)

    if coin_flip1 == "H" and coin_flip2 == "H":
        return 1
    else:
        return 0

def gen_graph(exact_value: float,
              n_runs: int,
              probs: list,
              runs: list) -> None:
    plt.hlines(exact_value, 0, n_runs, colors="brown", label="Valor Exato")
    plt.plot(runs, probs, label="Lançamento de duas moedas não viciadas")
    plt.xlabel("# Lançamentos")
    plt.ylabel("Probabilidades")
    plt.legend()
    plt.show()


if __name__ == "__main__":
    n_runs = 1000
    count = 0
    exact_value = 1/4

    probs = []
    runs = []

    for run in range(n_runs):
        count += flip_coins()
        probs.append(count/(run+1))
        runs.append(run+1)
    gen_graph(exact_value, n_runs, probs, runs)













