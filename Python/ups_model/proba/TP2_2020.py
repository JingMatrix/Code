# -*- coding: utf-8 -*-

import numpy as np
import matplotlib.pyplot as plt
import scipy.stats as scs

#%% Ex 1, fonctions
    
def simUnif(N,n):
    return np.floor(np.random.random_sample(size=n)*N)

def simExp(n):
    return -np.log(np.random.random_sample(size=n))

def simDemicercle(n):
    X = np.zeros(n)
    for i in range(n):
        Y = 2*np.random.random_sample()-1
        while np.random.random_sample() > np.sqrt(1-Y**2):
            Y = 2*np.random.random_sample()-1
        X[i] = Y
    return X

def sim0Z(n):
    Z = simExp(n) + simExp(n)
    return Z * np.random.random_sample(size=n)

def simLaplace(n):
    U = np.random.random_sample(size=n)
    return (2*(U>1/2)-1)*simExp(n)

def simGaussRejet(n):
    X = np.zeros(n)
    for i in range(n):
        Y = simLaplace(1)[0]
        while np.random.random_sample() > np.exp(-(np.abs(Y)-1)**2/2):
            Y = simLaplace(1)[0]
        X[i] = Y
    return X
    
#%% Tracés : Ex 1.1
n=10000
plt.figure()
plt.hist([simUnif(12,n),scs.randint(0,12).rvs(size=n)],bins=12)
plt.title("Loi uniforme sur {0,...,11}")
plt.show()
#%% Tracés : Ex 1.2
plt.figure()
plt.hist([simExp(n),scs.expon.rvs(size=n)],bins=12)
plt.title("Loi exponentielle")
plt.show()
#%% Tracés : Ex 1.3
plt.figure()
plt.hist([simDemicercle(n),scs.semicircular.rvs(size=n)],bins=12)
plt.title("Loi du demi-cercle")
plt.show()
#%% Tracés : Ex 1.4
plt.figure()
plt.hist([sim0Z(n),scs.expon.rvs(size=n)],bins=12)
plt.title("Loi de Unif([0,Z]) = loi exponentielle")
plt.show()
#%% Tracés : Ex 1.5
plt.figure()
plt.hist([simLaplace(n),scs.laplace.rvs(size=n)],bins=12)
plt.title("Loi de Laplace")
plt.show()
#%% Tracés : Ex 1.6
plt.figure()
plt.hist([simGaussRejet(n),scs.norm.rvs(size=n)],bins=12)
plt.title("Loi normale par méthode du rejet")
plt.show()

#%% Ex 2

def simPoi(l,n):
    rvs = np.zeros(n)
    U = np.random.random_sample(size=n)
    for i in range(n):
        k = 0
        kfact = 1
        p = np.exp(-l)
        while U[i] > p:
            k=k+1
            kfact = kfact *k
            p=p+np.exp(-l)*(l**k)/kfact
        rvs[i]=k
    return rvs

n=10000
plt.figure()
plt.step(np.sort(simPoi(2,n)),np.arange(0,1,1/n))
plt.step(np.sort(scs.poisson(2).rvs(size=n)),np.arange(0,1,1/n))
plt.title("Loi de Poisson")
plt.show()

#%% Ex 3

def simUnifDisk(n):
    X,Y = np.zeros(n),np.zeros(n)
    for i in range(n):
        X2,Y2 = np.random.random_sample(2)*2-1
        while X2**2+Y2**2 > 1:
            X2,Y2 = np.random.random_sample(2)*2-1
        X[i],Y[i] = X2,Y2
    return X,Y
    
plt.figure()
plt.scatter(*simUnifDisk(1000))
th = np.linspace(0,2*np.pi,1000)
plt.plot(np.cos(th),np.sin(th))
plt.show()

