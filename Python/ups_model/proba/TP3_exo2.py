# -*- coding: utf-8 -*-
"""
Created on Mon Jan 27 16:12:02 2020

@author: JingMatrix
"""


import numpy as np
import matplotlib.pyplot as plt
import scipy.stats as scs

# %%


def tire(white, ball):
    return scs.bernoulli(white/ball).ppf(np.random.random_sample(1))


def Polya(N):
    X = np.linspace(1, N + 1, N + 1)
    for k in range(1, N + 1):
        X[k] = tire(X[k-1], k+2) + X[k-1]
    return X

# %%


N = 1000
times = 5
Y = np.linspace(1, N + 1, N + 1)
plt.figure()
for t in range(0, times):
    plt.plot(Y, Polya(N)/(Y + 2))
plt.show()

# %%


def Polya2(N, a, b):
    X = np.linspace(1, N + 1, N + 1)
    X[0] = a
    for k in range(1, N + 1):
        X[k] = tire(X[k-1], k+a+b) + X[k-1]
    return X


N = 1000
times = 5
Y = np.linspace(1, N + 1, N + 1)
plt.figure()
for t in range(0, times):
    plt.plot(Y, Polya2(N, 3, 2)/(Y + 2))
plt.show()

# %%

plt.figure()
M = 1000
for N in [25, 50, 100]:
    for k in range(0, 1000):
        X = scs.randint(1, N + 2).ppf(np.random.random_sample(M))
    plt.step(np.sort(X), np.arange(0, 1, 1./(M)))
plt.show()
