# -*- coding: utf-8 -*-
"""
Created on Mon Mar  2 15:43:32 2020

@author: JingMatrix
"""
import numpy as np
import matplotlib.pyplot as plt


# %% System


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


# %% Quelque curiosité


theta0, theta0p = np.pi/2, 0
theta1, theta1p = np.pi/4, 0
T, N = 100, 10000
t = np.linspace(0, T, N)
alpha = 0
X1 = euler(systemf, [theta0, theta0p], t, alpha)
X2 = euler(systemf, [theta1, theta1p], t, alpha)
plt.figure()
plt.subplot(1, 3, 1)
plt.plot(t, X1[:-1, 0])
plt.plot(t, X2[:-1, 0])
plt.legend(["theta = pi/2", "theta = pi/4"])
plt.title("Theta(t) v.s t")
plt.subplot(1, 3, 2)
plt.plot(X1[:-1, 0], X1[:-1, 1])
plt.legend(["theta = pi/2"])
plt.title("Theta(t) v.s Theta'(t)")
plt.subplot(1, 3, 3)
plt.plot(X2[:-1, 0], X2[:-1, 1])
plt.legend(["theta = pi/4"])
plt.title("Theta(t) v.s Theta'(t)")
plt.show()

# %% Objective 1 We simulate the limit value of theta

theta0, theta0p = 0, 100
T, N = 1000, 10000
t = np.linspace(0, T, N)
alpha = 1
X = euler(systemf, [theta0, theta0p], t, alpha)
plt.figure()
plt.subplot(1, 2, 1)
plt.plot(t, X[:-1, 0]/np.pi)
plt.title("Theta(t)/pi v.s t")
n = round(X[-1, 0]/np.pi)
plt.axhline(n, color='r')
plt.legend(["theta(t)/pi", "%d" % n])
plt.subplot(1, 2, 2)
plt.plot(X[:-1, 0], X[:-1, 1])
plt.title("Theta(t) v.s Theta'(t)")
plt.show()
print("We know that in this case the limit is %d pi" % n)
thetap = np.linspace(0, 100, 30)
Y = [round(euler(systemf, [theta0, theta0p], t, alpha)[-1, 0]/np.pi)
     for theta0p in thetap]
plt.figure()
plt.plot(thetap, Y)
plt.show()

# %% Objective 2

theta0, theta0p = 0, 0.01
T, N = 105, 10000
t = np.linspace(0, T, N)
alpha1, alpha2 = 0, 0.001
X1 = euler(systemf, [theta0, theta0p], t, alpha1)
X2 = euler(systemf, [theta0, theta0p], t, alpha2)
plt.figure()
plt.plot(t, X1[:-1, 0])
plt.plot(t, X2[:-1, 0])
plt.legend(["alpha = 0", "alpha = 0.001"])
plt.show()