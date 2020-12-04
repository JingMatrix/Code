# -*- coding: utf-8 -*-
"""
Created on Thu Apr 16 16:45:20 2020

@author: JingMatrix
"""

import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import odeint
from scipy.optimize import newton

# %%


def f(X, t):
    return np.array([X[1], -np.sin(X[0])])


t = np.linspace(0, 20, 50000)

x0 = np.array([3.1, 0.])

# %%


def euler(f, x0, t):
    n = len(t)
    x = x0
    for k in range(0, n-1):
        h = t[k+1] - t[k]
        p1 = f(x[k], t[k])
        x.append(x[k] + h * p1)
    return x


def rk4(f, x0, t):
    n = len(t)
    x = x0
    for k in range(0, n-1):
        h = t[k+1] - t[k]
        p1 = f(x[k], t[k])
        p2 = f(x[k] + h * p1 / 2, t[k] + h / 2)
        p3 = f(x[k] + h * p2 / 2, t[k] + h / 2)
        p4 = f(x[k] + h * p3, t[k+1])
        x.append(x[k] + h * (p1+2*p2+2*p3+p4) / 6)
    return x


def eulerbis(f, x0, t):
    n = len(t)
    x = x0
    for k in range(0, n-1):
        h = t[k+1] - t[k]
        s = newton(lambda u: u - x[k] - f(u, t[k+1]) * h, x[k])
        x.append(s)
    return x


# %%
w = 4
Y, X = np.mgrid[-w:w:100j, -w:w:100j]
[U, V] = f([X, Y], 0)
plt.figure()
plt.streamplot(X, Y, U, V, density=[0.5, 0.7])
plt.show()

# %%
x = odeint(f, x0, t)
x1 = np.stack(euler(f, [x0], t), 0)
x3 = np.stack(rk4(f, [x0], t), 0)
x4 = np.stack(eulerbis(f, [x0], t), 0)

# %%
plt.figure()
plt.plot(x[:, 0], x[:, 1])
plt.title(r"solution de $x'$ vs $x$")
plt.show()

# %%
plt.figure()
plt.plot(x[:, 0], x[:, 1], '--', label='Solution exacte')
plt.plot(x1[:, 0], x1[:, 1], label="Méthode d'Euler")
plt.title("Méthode d'Euler")
plt.legend(loc='upper left')
plt.show()

plt.figure()
plt.plot(x[:, 0], x[:, 1], '--', label='Solution exacte')
plt.plot(x1[:, 0], x3[:, 1], label="Méthode de Runge-Kutta")
plt.title("Méthode de Runge-Kutta")
plt.legend(loc='upper left')
plt.show()

plt.figure()
plt.plot(x[:, 0], x[:, 1], '--', label='Solution exacte')
plt.plot(x4[:, 0], x4[:, 1], label="Méthode d'Euler Implicite")
plt.title("Méthode d'Euler implicite")
plt.legend(loc='best')
plt.show()

# %%
plt.figure()
plt.plot(t, x[:, 0], '--', label='Solution exacte')
plt.plot(t, x1[:, 0], label="Méthode d'Euler")
plt.title("Méthode d'Euler")
plt.legend(loc='upper left')
plt.show()

plt.figure()
plt.plot(t, x[:, 0], '--', label='Solution exacte')
plt.plot(t, x3[:, 0], label="Méthode de Runge-Kutta")
plt.title("Méthode de Runge-Kutta")
plt.legend(loc='upper left')
plt.show()


plt.figure()
plt.plot(t, x[:, 0], '--', label='Solution exacte')
plt.plot(t, x4[:, 0], label="Méthode d'Euler Implicite")
plt.title("Méthode d'Euler implicite")
plt.legend(loc='best')
plt.show()