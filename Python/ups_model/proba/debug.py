import numpy as np
import scipy.stats as scs
import matplotlib.pyplot as plt
import math

M = 10
# %% Exo2


def fac(X):
    for i in range(len(X)):
        X[i] = math.factorial(np.int(X[i]))
    return X


def comPos(v, lam):
    comp = 1
    N = 0
    v = v*np.exp(lam)
    while comp == 1 and N <= 11:
        N = N+1
        if v < np.sum(lam**np.arange(N+1)/fac(np.arange(N+1))):
            comp = 0
    return N-1


def simPos(N, lam):
    X = []
    for i in range(N):
        u = np.random.random_sample()
        X.append(comPos(u, lam))
    return X


X7 = simPos(M, 2)
plt.figure()
plt.hist(X7, bins=12, density=True)
plt.legend(["Simulation", "From Scipy"])
plt.show()


