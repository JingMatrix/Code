# -*- coding: utf-8 -*-
"""
Created on Mon Feb 10 15:49:03 2020

@author: JingMatrix
"""

import numpy as np
import matplotlib.pyplot as plt

# %% data in Nil.txt

M = np.loadtxt("Nil.txt")


def rohat(X, k):
    n = len(X)-1
    r0 = 1/(n+1)*np.sum((X[0:n]-np.mean(X))*(X[0:n]-np.mean(X)))
    return 1/(n-k+1)*np.sum((X[0:n-k]-np.mean(X))*(X[k:n]-np.mean(X)))/r0


K = 30
X = np.arange(0, K+1)
rohat_n = np.zeros(K+1)
for k in X:
    rohat_n[k] = rohat(M[:, 1], k)

plt.figure()
plt.scatter(X, rohat_n)
plt.title("Valeur de ro_n(k) for k <= 30")
plt.xlabel("k")
plt.ylabel("ro^k")
plt.show()

print("rohat_n is decreasing w.s.t k and with a minimal nonzero")
print("Therefore, X_k are not independent")
# %% Calculate Y

miu = np.mean(M[:, 1])
Y = np.cumsum(M[:, 1]-miu)

X = np.arange(0, len(Y))
plt.figure()
plt.plot(X, Y)
plt.title("Valeur de Y(k)")
plt.xlabel("k")
plt.ylabel("Y(k)")
plt.show()


# %% variation quadratiques

def S(n, a):
    m = int(n/a)-1
    V = []
    for t in range(m):
        V.append((Y[a*(t+2)]-2*Y[a*(t+1)]+Y[a*t])**2)
    return np.mean(V)


n = len(Y)-1
m = 31
X = np.arange(1, m)
S_n = []
for a in X:
    S_n.append(S(n, a))
plt.figure()
plt.plot(X, S_n)
plt.xscale("log")
plt.yscale("log")
plt.title("Valeur de S_n(a)")
plt.xlabel("a")
plt.ylabel("S_n(a)")
plt.show()

print("From the graph, it is almost linear")

# %% estimator of H


def estimate_coef(x, y):
    # number of observations/points
    n = np.size(x)
    # mean of x and y vector
    m_x, m_y = np.mean(x), np.mean(y)
    # calculating cross-deviation and deviation about x
    SS_xy = np.sum(y*x) - n*m_y*m_x
    SS_xx = np.sum(x*x) - n*m_x*m_x

    # calculating regression coefficients
    b_1 = SS_xy / SS_xx
    b_0 = m_y - b_1*m_x

    return(b_0, b_1)


def plot_regression_line(x, y, b):
    # plotting the actual points as scatter plot
    plt.scatter(x, y, color="m",
                marker="o", s=30)
    # predicted response vector
    y_pred = b[0] + b[1]*x

    # plotting the regression line
    plt.plot(x, y_pred, color="g")

    # putting labels
    plt.xlabel('x')
    plt.ylabel('y')

    # function to show plot
    plt.show()


x = np.log(np.arange(1, m))
y = np.log(S_n)

# estimating coefficients
b = estimate_coef(x, y)
print("Estimated coefficients:\nb_0 = {}\nb_1 = {}".format(b[0], b[1]))

# plotting regression line
plot_regression_line(x, y, b)
print("H =", b[1]/2)

Coe = np.polyfit(x, y, 1)

print("H by polyfit is", Coe[0]/2)
