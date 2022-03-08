"""Coin Dice Experiments

Lançamento de uma moeda justa: S = {h, t} => P(h) = P(t) = 1/2
A = {sair H}

Lançamento de duas moedas justas: S = {hh, ht, th, tt} => P(hh) = 1/4
A = {ambas sairem h}
"""

import numpy as np
import matplotlib.pyplot as plt

def do_coin_exp() -> int:
    coin1 = ['h', 't']
    coin2 = ['h', 't']
    flip_coin1 = np.random.choice(coin1)
    flip_coin2 = np.random.choice(coin2)
    if flip_coin1 == 'h' and flip_coin2 == 'h':
        return 1
    else:
        return 0

def plot_results(exact_value, n_runs, probs, runs):
    plt.hlines(exact_value, 0, n_runs, colors='brown', label='valor exato =     1/4')
    plt.plot(runs, probs, label='Lançamento de uma moeda')
    plt.xlabel('# de lançamentos')
    plt.ylabel('Probabilidade de sair {h}')
    plt.legend()
    plt.show()



if __name__ == "__main__":
    n_runs = 10000
    count = 0
    exact_value = 1/4

    probs = []
    runs = []

    for run in range(n_runs):
        count += do_coin_exp()
        probs.append(count/(run+1))
        runs.append(run+1)

    plot_results(exact_value, n_runs, probs, runs)
