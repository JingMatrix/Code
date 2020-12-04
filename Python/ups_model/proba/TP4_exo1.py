# -*- coding: utf-8 -*-
"""
Created on Mon Feb  3 15:48:43 2020

@author: JingMatrix
"""

import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import minimize_scalar
import scipy.stats as scs
from scipy.special import gamma

# %% question 3


orages = np.loadtxt('Orages.txt')
plt.figure()
plt.hist(orages, bins=16, density=True)
plt.show()

# %% question 4

# moyenne emprique
N = len(orages)
moyenneEmp = np.cumsum(orages)/np.arange(1, N+1)

# mediane

median = np.median(orages)

# plot
plt.figure()
plt.axhline(median, color="black")
plt.plot(np.arange(1, N+1), moyenneEmp)
plt.title("moyenne empirique et mediane empirique")
plt.show()

# %% question 5

# calculate moments

m1 = np.mean(orages)
m2 = np.mean(orages**2)
alpha_MM = m1**2 / (m2 - m1**2)
beta_MM = m1 / (m2 - m1**2)

# calculate maximun likelihood estimation


def f(x):
    return np.log(gamma(x)) + x*(1 - np.log(x)
                                 + np.log(np.mean(orages))
                                 - np.mean(np.log(orages)))


alpha_ML = minimize_scalar(f).x
beta_ML = alpha_ML / np.mean(orages)


# %% question 6

Ga = scs.gamma(alpha_MM, scale=1 / beta_MM)

X = np.linspace(0, max(orages), 1000)
plt.figure()
plt.step(np.sort(orages), np.arange(0, 1, 1./len(orages)))
plt.plot(X, Ga.cdf(X))
plt.show()

# Therefore gamma distribution is a good model for this data

# %% question 7

Ga = scs.gamma(alpha_ML, scale=1 / beta_ML)

X = np.linspace(0, max(orages), 1000)
plt.figure()
plt.step(np.sort(orages), np.arange(0, 1, 1./len(orages)))
plt.plot(X, Ga.cdf(X))
plt.show()

# Therefore gamma distribution is a good model for this data
