# -*- coding: utf-8 -*-
"""
Created on Mon Jan 27 15:44:31 2020

@author: JingMatrix
"""


import numpy as np
import matplotlib.pyplot as plt
import scipy.stats as scs

# %%
N = 10000
X = np.random.random_sample(N)
S = np.cumsum(X)
k = range(1, N+1)
plt.figure()
plt.subplot(2, 1, 1)
plt.plot(k, S/k)
plt.axhline(1.0/2)
plt.subplot(2, 1, 2)
plt.xscale("log")
plt.plot(k, S/k)
plt.axhline(1.0/2)
plt.show()

# %%

M = 5
X = np.random.random_sample(M)
S = np.cumsum(X)
k = range(1, M+1)
plt.figure()
plt.subplot(2, 1, 1)
plt.plot(k, S/k)
# plt.axhline(1.0/2)
plt.subplot(2, 1, 2)
plt.xscale("log")
plt.plot(k, S/k)
# plt.axhline(1.0/2)
plt.show()

print("No rule obvious can be found when M = 5")

# %%

N = 10000
X = scs.cauchy().ppf(np.random.random_sample(N))
S = np.cumsum(X)
k = range(1, N+1)
plt.figure()
plt.subplot(2, 1, 1)
plt.plot(k, S/k)
plt.subplot(2, 1, 2)
plt.xscale("log")
plt.plot(k, S/k)
plt.show()
