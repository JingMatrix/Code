# -*- coding: utf-8 -*-
"""
Created on Sat Feb 22 15:31:16 2020

@author: JingMatrix
"""

# -*- coding: utf-8 -*-
import matplotlib.pyplot as plt
import numpy as np
import scipy.stats as scs


def TraceFctRepEmpirique(sample):
    n = len(sample)
    plt.step(np.sort(sample), np.arange(n)/n)


# %% Exo1 Q3
def simDemiCercle(n):
    X = np.zeros(n)
    for i in range(n):
        U, V = 2, 0
        while U >= np.sqrt(1-V**2):
            U, V = np.random.random_sample(), 2*np.random.random_sample()-1
        X[i] = V
    return X


def pdfDemiCercle(x):
    return 2/np.pi*np.sqrt(1-x**2)


n = 10000
sample = simDemiCercle(n)
plt.figure()
X = np.linspace(-1, 1, 100)
plt.hist(sample, density=True, bins=30)
plt.plot(X, pdfDemiCercle(X))
plt.show()


# %% Exo2 Q5


def rec(mu, sigma, N):
    X = scs.norm.rvs(size=N)
    Y = np.zeros(N+1)
    Y[0] = 1
    for n in range(N):
        Y[n+1] = np.exp(mu + sigma*X[n])*Y[n]+1
    return Y


# %% Exo2 Q6, Quelques tracés

N = 100
plt.figure()
for i in range(5):
    Y = rec(1, 1, N)
    plt.subplot(2, 2, 1)
    plt.plot(Y)
    plt.subplot(2, 2, 2)
    plt.plot(Y)
    plt.yscale('log')
    Y = rec(-1, 1, N)
    plt.subplot(2, 2, 3)
    plt.plot(Y)
    plt.subplot(2, 2, 4)
    plt.plot(Y)
    plt.yscale('log')
plt.show()

# %% Exo2 Q8, Théorème ergodique

N = 10000
plt.figure()
for m in range(30):
    Y = rec(-1, 1, N)
    N2 = np.cumsum(Y <= 2)/np.arange(1, N+2)
    plt.subplot(1, 2, 1)
    plt.plot(N2)
    plt.subplot(1, 2, 2)
    plt.plot(N2)
    plt.xscale('log')
    # plt.yscale('log')
plt.show()

# %% Exo2 Q10


def recM(mu, sigma, N, M):
    X = scs.norm.rvs(size=(N, M))
    Y = np.zeros(shape=(N+1, M))
    Y[0] = 1
    for n in range(N):
        Y[n+1] = np.exp(mu + sigma*X[n])*Y[n]+1
    return Y


# %% Exo2 Q11, Convergence en loi quand mu < 0


N = 100
M = 1000
Y = recM(-1, 1, N, M)
plt.figure()
for n in [20, 50, 100]:
    plt.subplot(2, 2, 1)
    TraceFctRepEmpirique(Y[n])
    plt.subplot(2, 2, 2)
    TraceFctRepEmpirique(Y[n])
    plt.xscale('log')
    plt.subplot(2, 2, 3)
    plt.hist(Y[n], histtype='step', density=True, bins=30)
    plt.subplot(2, 2, 4)
    plt.hist(np.log(Y[n]), histtype='step', density=True, bins=30)
plt.show()

# %% Bonus: asympotique de la fct. de repartition quand mu < 0

N = 100
M = 1000
Y = recM(-1, 1, N, M)
plt.figure()
plt.step(np.sort(Y[N]), np.arange(M, 0, -1)/M)
plt.xscale('log')
plt.yscale('log')
plt.show()

# %% Bonus: comparaison de fct. de repartition empirique avec moyenne de Césaro

N = 1000
M = 1000
Y = recM(-1, 1, N, M)
plt.figure()
plt.subplot(1, 2, 1)
TraceFctRepEmpirique(Y[N])
TraceFctRepEmpirique(Y[:, M-1])
plt.xscale('log')
plt.subplot(1, 2, 2)
plt.hist(np.log(Y[N]), histtype='step', density=True, bins=20)
plt.hist(np.log(Y[:, M-1]), histtype='step', density=True, bins=20)
plt.show()


# %% Bonus: double moyenne (sur n et sur m) des fonctions de répartition
# empiriques
N = 1000
M = 1000
Y = recM(-1, 1, N, M)
Yf = Y[100:, :].flatten()
plt.figure()
plt.subplot(2,2,1)
TraceFctRepEmpirique(Yf)
plt.subplot(2,2,2)
TraceFctRepEmpirique(Yf)
plt.xscale('log')
plt.subplot(2,2,3)
plt.hist(Yf,histtype='step',density=True,bins=30)
plt.subplot(2,2,4)
plt.hist(np.log(Yf),histtype='step',density=True,bins=30)
plt.show()
plt.figure()
plt.step(np.sort(Yf),np.arange(len(Yf),0,-1)/len(Yf))
plt.xscale('log')
plt.yscale('log')
plt.show()