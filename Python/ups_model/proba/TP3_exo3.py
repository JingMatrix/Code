# -*- coding: utf-8 -*-
"""
Created on Mon Jan 27 17:19:03 2020

@author: JingMatrix
"""

import numpy as np
import matplotlib.pyplot as plt

# %%


def DistanceToUnif(X, re_array):
    X = np.sort(X)
    size = len(X)
    D = np.linspace(1, size, size)
    if re_array == 1:
        for n in range(1, size + 1):
            D[n] = max(np.max(np.linspace(1, n, n)/n - X),
                       np.max(X - np.linspace(0, n-1, n)/n))
        return D
    else:
        n = size
        return max(np.max(np.linspace(1, n, n)/n - X),
                   np.max(X - np.linspace(0, n-1, n)/n))


# %%


N = 5000
plt.figure()
re_array = 1
for k in range(0, 5):
    plt.subplot(5, 1, k + 1)
    X = np.random.random_sample(N)
    plt.plot(np.linspace(1, N, N), DistanceToUnif(X, re_array))
plt.show()
