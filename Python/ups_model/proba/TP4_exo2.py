# -*- coding: utf-8 -*-
"""
Created on Mon Feb  3 16:43:41 2020

@author: JingMatrix
"""

import numpy as np
import matplotlib.pyplot as plt
import scipy.stats as scs

# %% questuon 4

# By scale sample with a real theta, we get data following N(1, 1) from data
# following N(theta, theta**2)


# %% question 5

M = 5
N = 1000
plt.figure()
for m in range(0, 5):
    X = scs.norm.rvs(loc=1, size=N)
    moment1Emp = np.cumsum(X)/np.arange(1, N+1)
    moment2Emp = np.cumsum(X**2)/np.arange(1, N+1)
    theta = - moment1Emp/2 + (moment2Emp + 0.25*moment1Emp**2)**0.5
    plt.plot(np.arange(1, N+1), theta)
plt.show()

# %% question 6

# for maximun likelihood estimation
M = 1000
R = np.zeros(8)
for n in range(3, 11):
    theta = np.zeros(M)
    for i in range(0, M):
        X = scs.norm.rvs(loc=1, size=2**n)
        theta[i] = -np.mean(X)/2 + (np.mean(X**2) + 0.25*np.mean(X)**2)**0.5
    R[n - 3] = np.mean((theta - 1)**2)

# for moment 1 estimation
Moment1 = np.zeros(8)
for n in range(3, 11):
    theta = np.zeros(M)
    for i in range(0, M):
        X = scs.norm.rvs(loc=1, size=2**n)
        theta[i] = np.mean(X)
    Moment1[n - 3] = np.mean((theta - 1)**2)

# for moment 2 estimation
Moment2 = np.zeros(8)
for n in range(3, 11):
    theta = np.zeros(M)
    for i in range(0, M):
        X = scs.norm.rvs(loc=1, size=2**n)
        theta[i] = (np.mean(X**2)*0.5)**0.5
    Moment2[n - 3] = np.mean((theta - 1)**2)

# plot the quadratic risk
plt.figure()
Y = 2**np.arange(3, 11)
plt.xscale("log")
plt.plot(Y, R*Y)
plt.plot(Y, Moment1*Y)
plt.plot(Y, Moment2*Y)
plt.legend(['ML estimation', "Moment1 estimation", "Moment2 estimation"])
plt.show()

# %% question 7

# Moment2 estimation and ML estimation are significant better then Moment1
# estimation with respect to quadratic risk function.
# ML estimation is slightly better then Moment2 estimation


# %% question 9

# for maximun likelihood estimation
M = 1000
T = 10
R = np.zeros(T)
for n in range(3, T + 3):
    theta = np.zeros(M)
    for i in range(0, M):
        X = scs.norm.rvs(loc=1, size=2**n)
        theta[i] = -np.mean(X)/2 + (np.mean(X**2) + 0.25*np.mean(X)**2)**0.5
    R[n - 3] = np.mean((theta - 1)**2)

plt.figure()
Y = 2**np.arange(3, 3 + T)
plt.xscale("log")
plt.ylim(0, 0.7)
plt.plot(Y, R*Y)
plt.axhline(1/3, color="black")
plt.title("the asymptotic behavior of ML estimation")
plt.show()

# %% question 10
