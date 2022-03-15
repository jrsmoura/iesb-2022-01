import numpy as np
import matplotlib.pyplot as plt


def graph(_n_runs: int,
          _runs: list,
          _probs: list,
          _x_in: list,
          _y_in: list,
          _x_out: list,
          _y_out: list
          ) -> None:
    fig = plt.figure(figsize=(8, 5))
    ax1 = fig.add_subplot(111)
    ax2 = fig.add_subplot(222)
    ax1.hlines(np.pi, 0, _n_runs, colors="brown", label="Valor Exato", linewidth=1)
    ax1.plot(_runs, _probs, label="Resultados", alpha=0.3, color='blue')
    ax1.set_xlabel("# Lançamentos")
    ax1.set_ylabel("Valor Simulado")
    ax1.legend(loc=4)
    ax2.scatter(_x_in, _y_in, color='blue', alpha=0.1)
    ax2.scatter(_x_out, _y_out, color='brown', alpha=0.1)
    ax2.set_xlim([0, 1])
    ax2.set_ylim([0, 1])
    plt.show()


if __name__ == '__main__':
    n_runs = 10000
    runs = []
    hits = []
    x_in = []
    y_in = []
    x_out = []
    y_out = []
    n_hits = 0

    for run in range(n_runs):
        x = np.random.rand()
        y = np.random.rand()
        if x ** 2 + y ** 2 <= 1:
            x_in.append(x)
            y_in.append(y)
            n_hits += 1
        else:
            x_out.append(x)
            y_out.append(y)
        runs.append(run + 1)
        hits.append(4 * n_hits / (run + 1))

    graph(n_runs, runs, hits, x_in, y_in, x_out, y_out)
