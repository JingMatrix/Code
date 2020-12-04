# -*- coding: utf-8 -*-
# Python < 3 has been commented for running on Python > 3

import matplotlib.pyplot as plt
import numpy as np
import scipy.stats as scs
import scipy as sp

# %% Exercice 1 - histogramme

Orages = np.loadtxt('Orages.txt')

# On peut reprÃ©senter ces donnÃ©es Ã  l'aide d'un histogramme :

plt.figure()
plt.hist(Orages, bins=16, normed=True)
plt.title(u'RÃ©partition des quantitÃ©s de pluie')
plt.xlabel(u'QuantitÃ© de pluie en Inch')
plt.show()

# %% Exo 1 - moyenne et mÃ©diane empirique

print('La moyenne empirique vaut : ', np.mean(Orages))
print('La mÃ©diane empirique vaut : ', np.median(Orages))

# %% Exo 1 - mÃ©thode des moments

MU1 = np.mean(Orages)
MU2 = np.mean(Orages**2)
amm = MU1**2/(MU2-MU1**2)  # Estimateur de alpha
bmm = MU1/(MU2-MU1**2)  # Estimateur de beta

# %% Exo 1 - maximum de vraisemblance


def loglikelihood(X, a):
    mu = np.mean(X)
    logmu = np.mean(np.log(X))
    return (a-1)*logmu - np.log(sp.special.gamma(a)) - a*np.log(mu)\
        + a*np.log(a)-a


def MLestimator(X):
    a = sp.optimize.minimize_scalar(lambda a: -loglikelihood(X, a)).x
    return a, a/np.mean(X)


aml, bml = MLestimator(Orages)

# %% Exo 1 - tracÃ©s

X = np.linspace(0, 2.5, 1000)
plt.figure()
plt.hist(Orages, bins=16, density=True, label='Histogramme renormalisÃ©')
Y = scs.gamma.pdf(X, amm, scale=1/bmm)
plt.plot(X, Y, label='DensitÃ© de la loi ajustÃ©e (mÃ©thode des moments)')
Y = scs.gamma.pdf(X, aml, scale=1/bml)
plt.plot(X, Y, label='DensitÃ© de la loi ajustÃ©e (ML)')
plt.legend()
plt.ylim(0, 5)
plt.show()

X = np.linspace(0, 2.5, 1000)
plt.figure()
plt.step(np.sort(Orages), np.arange(0, 1, 1/len(Orages)),
         label='Fonction de rÃ©partition empirique')
Y = scs.gamma.cdf(X, amm, scale=1/bmm)
plt.plot(X, Y, label='Fonction \
         de rÃ©partition ajustÃ©e (mÃ©thode des moments)')
Y = scs.gamma.cdf(X, aml, scale=1/bml)
plt.plot(X, Y, label='Fonction de rÃ©partition ajustÃ©e (ML)')
plt.legend()
plt.show()


# %% Exo 2 - theta chapeau en fonction de n

def thchapeau(X):
    m1 = np.mean(X)
    m2 = np.mean(X**2)
    return -m1/2+np.sqrt(m2+m1**2/4)


M = 5
theta = 1
plt.figure()
for i in range(M):
    X = scs.norm.rvs(size=1000, loc=theta, scale=theta)
    thetachapeau = [thchapeau(X[:n+1]) for n in range(1000)]
    plt.plot(range(1, 1001), thetachapeau)
plt.legend()


# %% Exo 2 - estimation du risque

M = 1000
theta = 1
plt.figure()
ns = 2**np.arange(3, 11)
risk_thchapeau = []
risk_mean = []
risk_std = []
for n in ns:
    X = scs.norm.rvs(size=(M, n), loc=theta, scale=theta)
    m1 = np.mean(X, axis=1)
    m2 = np.mean(X**2, axis=1)
    sigma = np.std(X, axis=1)
    thetachapeau = -m1/2+np.sqrt(m2+m1**2/4)
    risk_thchapeau.append(n*np.mean((thetachapeau-theta)**2))
    risk_mean.append(n*np.mean((m1-theta)**2))
    risk_std.append(n*np.mean((sigma-theta)**2))
plt.scatter(ns, risk_thchapeau, label="ML")
plt.scatter(ns, risk_mean, label="moyenne")
plt.scatter(ns, risk_std, label="Ã©cart-type")
plt.xscale('log')
plt.legend()


# %% Exo 2 - l'asymptotique du risque

print("constante limite, ML: ", np.mean(risk_thchapeau))
print("constante limite, moyenne: ", np.mean(risk_mean))
print("constante limite, Ã©cart-type: ", np.mean(risk_std))


# %% Exo 2 - convergence en loi

M = 1000
theta = 1
plt.figure()
for n in 10, 100, 1000:
    X = scs.norm.rvs(size=(M, n), loc=theta, scale=theta)
    m1 = np.mean(X, axis=1)
    m2 = np.mean(X**2, axis=1)
    thetachapeau = -m1/2+np.sqrt(m2+m1**2/4)
    plt.hist(np.sqrt(3*n)*(thetachapeau-theta), histtype="step", bins=15,
             density=True, label="n="+str(n))
plt.legend()

# %% Exo 2 - intervalle de confiance

theta = 1
alpha = 0.2
n = 1000
X = scs.norm.rvs(size=n, loc=theta, scale=theta)
m1 = np.mean(X)
m2 = np.mean(X**2)
thetachapeau = -m1/2+np.sqrt(m2+m1**2/4)
print("point bord Ã  gauche de l'intervalle de confiance : ",
      thetachapeau - 1/np.sqrt(3*n)*scs.norm.ppf(1-alpha/2))
print("point bord Ã  gauche de l'intervalle de confiance : ",
      thetachapeau + 1/np.sqrt(3*n)*scs.norm.ppf(1-alpha/2))


theta = 1
alpha = 0.2
n = 1000
for i in range(10):
    X = scs.norm.rvs(size=n, loc=theta, scale=theta)
    m1 = np.mean(X)
    m2 = np.mean(X**2)
    thetachapeau = -m1/2+np.sqrt(m2+m1**2/4)
    if np.abs(theta - thetachapeau) < 1/np.sqrt(3*n)*scs.norm.ppf(1-alpha/2):
        print('theta est incluse dans l\'intervalle de confiance')
    else:
        print('theta n\'est PAS incluse dans l\'intervalle de confiance')
