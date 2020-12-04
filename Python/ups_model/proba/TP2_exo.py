# -*- coding: utf-8 -*-
"""
Created on Thu Feb 13 14:12:14 2020

@author: JingMatrix
"""


import numpy as np
import scipy.stats as scs
import matplotlib.pyplot as plt
import math


N = 10000
# %%Exo1.1

X1 = [np.floor(12*np.random.random_sample(size=N)), scs.randint(0, 12).rvs(N)]
plt.figure()
plt.hist(X1, bins=12, density=True)
plt.legend(["Simulation", "From Scipy"])
plt.show()

# %%Exo1.2
X2 = [-np.log(1-scs.uniform.rvs(size=N)), scs.expon().rvs(N)]
plt.figure()
plt.hist(X2, bins=12, density=True)
plt.legend(["Simulation", "From Scipy"])
plt.show()

# %%Exo1.3


def rejSemiC(N):
    X = []
    for i in range(N):
        while len(X) == i:
            U = np.random.random_sample(2)
            if 1-(2*U[0]-1)**2 >= (2*U[1])**2:
                X.append(2*U[0]-1)
    return X


X3 = [rejSemiC(N), scs.semicircular().rvs(N)]
plt.figure()
plt.hist(X3, bins=12, density=True)
plt.legend(["Simulation", "From Scipy"])
plt.show()

# %%Exo1.4

X4 = [(-np.log(1-scs.uniform.rvs(size=N))-np.log(1-scs.uniform.rvs(size=N)))
      * scs.uniform.rvs(size=N), scs.gamma(2).rvs(N)*scs.uniform().rvs(N)]
plt.figure()
plt.hist(X4, bins=12, density=True)
plt.legend(["Simulation", "From Scipy"])
plt.show()

# %%Exo1.5


def conLa(N):
    X = []
    for i in range(N):
        while len(X) == i:
            y = -np.log(1-scs.uniform.rvs())
            if y >= 0:
                X.append(y)
    return X


X5 = [conLa(N)*np.sign(np.random.random_sample(N)-0.5),
      scs.laplace.rvs(size=N)]
plt.figure()
plt.hist(X5, bins=12, density=True)
plt.legend(["Simulation", "From Scipy"])
plt.show()

# %%Exo1.6


def rejNorm(N):
    X = []
    for i in range(N):
        while len(X) == i:
            u = np.random.random_sample(2)
            v = conLa(1)[0]*np.sign(u[0]-0.5)
            # v = scs.laplace.rvs()
            if np.exp(-v**2/2) >= u[1]*np.exp((1-2*np.abs(v))/2):
                X.append(v)
    return X


X6 = [rejNorm(N), scs.norm().rvs(N)]
plt.figure()
plt.hist(X6, bins=12, density=True)
plt.legend(["Simulation", "From Scipy"])
plt.show()

# %% Exo2
lam = 2


def invPos(v, lam):
    comp = 1
    N = 0
    v = v*np.exp(lam)
    p = 1
    while comp == 1:
        if v < p:
            comp = 0
        N = N+1
        p = p + lam**N/math.factorial(N)
    return N-1


def simPos(N, lam):
    X = []
    for i in range(N):
        u = np.random.random_sample()
        X.append(invPos(u, lam))
    return X


X = np.linspace(0, 1, N)
plt.figure()
plt.step(np.sort(simPos(N, lam)), X)
plt.step(np.sort(scs.poisson(lam).rvs(size=N)), X)
plt.legend(["Simulation", "From Scipy"])
plt.show()

# X7 = [simPos(N, lam), scs.poisson(2).rvs(N)]
# plt.figure()
# plt.hist(X7, bins=12, density=True)
# plt.legend(["Simulation", "From Scipy"])
# plt.show()
