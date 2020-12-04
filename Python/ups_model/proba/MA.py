# -*- coding: utf-8 -*-
"""
Created on Mon Feb 24 15:47:40 2020

@author: JingMatrix(Jianyu MA)
"""
import numpy as np
import matplotlib.pyplot as plt
import scipy.stats as scs

# %% Exo 1.3


def GaltonWatson(N, theta):
    Z = np.zeros(N+1)
    Z[0] = 1
    for i in range(N):
        Z[i+1] = scs.poisson(theta*Z[i]).rvs()
    return Z


# %% Exo 1.4


def SamplePathZ(N, M, theta):
    plt.figure()
    for i in range(M):
        plt.plot(np.arange(N+1), GaltonWatson(N, theta))
    plt.title(r"%i smaple path with $\theta = %.1f $" % (M, theta))
    plt.show()
    return

# %% Exo 1.5


N, M, theta = 40, 20, 0.9
SamplePathZ(N, M, theta)

# %% Exo 1.6

N, M, theta = 40, 20, 1.1
SamplePathZ(N, M, theta)

# %% Exo 1.7


def SamplePathW(N, M, theta):
    plt.figure()
    for i in range(M):
        plt.plot(np.arange(N+1), GaltonWatson(N, theta)/theta**np.arange(N+1))
    plt.title("%i smaple path with W" %M)
    plt.show()
    return

# %% Exo 1.8

N, M, theta = 100, 20, 1.1
SamplePathW(N, M, theta)

# %% Exo 1.9

def EmpCdfW(N, M, theta):
    W = [(GaltonWatson(N, theta)/theta**np.arange(N+1))[N] for i in range(M)]
    plt.step(np.sort(W), np.arange(0, 1., 1/M))
    return

# %% Exo 1.10


M, theta = 500, 1.1
plt.figure()
for N in [10, 30, 50]:
    EmpCdfW(int(N), M, theta)
plt.legend(["N=10", "N=30", "N=50"])
plt.title("fonction empirique de W_N")
plt.show()
# %% Exo 1.11

def HitZero(N, M, theta):
    H = np.zeros(M) + N
    for i in range(M):
        Z =  GaltonWatson(N, theta)
        for t in range(N):
            if Z[t+1] == 0:
                H[i] = t+1
                break
    return H

# %% Exo 1.12


N, M, theta = 50, 400, 0.8
plt.figure()
plt.step(np.sort(HitZero(N, M, theta)), np.arange(1., 0, -1/M))
plt.yscale("log")
# %% Exo1.13

N, M, theta = 50, 400, 0.8
T = 300
D = [np.sort(HitZero(N, M, theta)), np.log(np.arange(1., 0, -1/M))]
est = np.polyfit(D[0], D[1], 1)
plt.figure()
plt.plot(D[0], D[1])
plt.plot(D[0], D[0]*est[0] + est[1])

print("estimation of alpha is :", np.exp(est[0]))

# result is -1.1265655113665285

plt.figure()
plt.plot(D[0], np.arange(1., 0, -1/M))
plt.plot(D[0], np.exp(D[0]*est[0] + est[1]))
