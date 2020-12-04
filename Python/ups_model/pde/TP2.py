# -*- coding: utf-8 -*-
"""
Created on Mon Mar  9 15:52:41 2020

@author: JingMatrix
"""
import numpy as np
import matplotlib.pyplot as plt

# %% system


def systemf(X, t, a):
    return np.array([X[1], -a*X[1]-np.sin(X[0])])


def pas_euler(systeme, h, tn, Yn, alpha):
    deriv = systeme(Yn, tn, alpha)
    return Yn+h*deriv


def euler(systeme, Yi, t, alpha):
    Y = Yi
    h = t[1]-t[0]
    liste_y = [Y]
    for tn in t:
        Y = pas_euler(systeme, h, tn, Y, alpha)
        liste_y.append(Y)
    return np.array(liste_y)


def phrase_plt(system, theta, T, N, alpha):
    t = np.linspace(0, T, N)
    X1 = euler(systemf, theta, t, alpha)
    plt.figure()
    plt.plot(X1[:-1, 0], X1[:-1, 1])
    plt.legend(["theta' = %.3f" % theta[1]])
    plt.title("Theta(t) v.s Theta'(t)")
    return


# def sol_plt(system, theta, T, N, alpha):
#     t = np.linspace(0, T, N)
#     X1 = euler(systemf, theta, t, alpha)
#     plt.figure()
#     plt.plot(X1[:-1, 0], X1[:-1, 1])
#     plt.legend(["theta' = %.3f" % theta[1]])
#     plt.title("Theta(t) v.s Theta'(t)")
#     return

# %% Exo 4 part 1


theta0 = 0
alpha = 1
T, N = 50, 100000
# plt.figure()
for theta0p in [0, 5, 10, 100]:
    phrase_plt(systemf, [theta0, theta0p], T, N, alpha)

plt.show()


# %% Exo 4 part 1

theta0 = 0
alpha = 1
T, N = 50, 1000
t = np.linspace(0, T, N)
Max = 10**2
plt.figure()
for step in [1, 10]:
    n = []
    for theta0p in np.arange(1, Max, step):
        X = euler(systemf, [theta0, theta0p], t, alpha)
        n.append(round(X[-1, 0]/np.pi))
    plt.plot(np.arange(1, Max, step), n)
plt.legend(["Step = 1", "Step = 10"])
plt.show()


# %% Exo 5 part 1

def theta0prime(alpha, depth, Range, epsilon, Interval):
    for i in range(depth):
        n_inf = []
        search_range = np.linspace(Interval[0], Interval[1], Range)
        for theta0p in search_range:
            X = euler(systemf, [theta0, theta0p], t, alpha)
            n_inf.append(round(X[-1, 0]/np.pi))
        print(n_inf)
        indexof2 = n_inf.index(2)
        Interval[1] = search_range[indexof2]
        Interval[0] = search_range[indexof2-1]
        # print(Interval[1]-Interval[0])
        if Interval[1]-Interval[0] < epsilon:
            break
    return np.mean(Interval)

# %% Exo 5 part 2


theta0 = 0
T, N = 500, 10000
t = np.linspace(0, T, N)
alphas = np.linspace(0.005, 0.1, 20)
depth = 3
Range = 100
epsilon = 0.001

X = [theta0prime(alpha, depth, Range, epsilon, [0, 5]) for alpha in alphas]
plt.figure()
plt.plot(alphas, X)
plt.title("theta0'(alpha) v.s. alpha ")
plt.show()


# %% debug

# plt.plot(alphas, X)
# plt.title("theta0'(alpha) v.s. alpha ")
# plt.show()