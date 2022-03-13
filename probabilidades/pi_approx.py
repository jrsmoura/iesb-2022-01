import numpy as np
import matplotlib.pyplot as plt


def graph(_n_runs: int,
          _runs: list,
          _probs: list,
          _x: list,
          _y: list) -> None:
    fig = plt.figure(figsize=(16, 12))
    ax1 = fig.add_subplot(111)
    ax2 = fig.add_subplot(222)
    ax1.hlines(np.pi, 0, _n_runs, colors="brown", label="Valor Exato", linewidth=1)
    ax1.plot(_runs, _probs, label="Resultados", alpha=0.3, color='blue')
    ax1.set_xlabel("# Lançamentos")
    ax1.set_ylabel("Valor Simulado")
    ax1.legend(loc=4)
    ax2.scatter(_x, _y, color='blue', alpha=0.1)
    ax2.set_xlim([0, 1])
    ax2.set_ylim([0, 1])
    plt.show()


if __name__ == '__main__':
    n_points = 10000
    n_runs = 10000
    runs = []
    hits = []
    x_hit = []
    y_hit = []
    n_hits = 0

    for run in range(n_runs):
        x = np.random.rand()
        y = np.random.rand()
        if x ** 2 + y ** 2 <= 1:
            x_hit.append(x)
            y_hit.append(y)
            n_hits += 1
        runs.append(run + 1)
        hits.append(4 * n_hits / (run + 1))

    graph(n_runs, runs, hits, x_hit, y_hit)
