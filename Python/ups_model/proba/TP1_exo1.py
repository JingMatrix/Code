# -*- coding: utf-8 -*-

import numpy as np
import matplotlib.pyplot as plt
import scipy.stats as scs


def dataX(k):
    if k >= 5:
        return np.linspace(0, 6, 1000)
    else:
        return np.linspace(-5,5,1000)

def dataY(k,l):
    if k == 1:
        return scs.norm(0,l).pdf(dataX(k))
    if k == 2:
        return scs.norm(0,l).cdf(dataX(k))
    if k == 3:
        return scs.cauchy().pdf(dataX(k))
    if k == 4:
        return scs.cauchy().cdf(dataX(k))
    if k == 5:
        return scs.gamma(l).pdf(dataX(k))
    if k == 6:
        return scs.gamma(l).cdf(dataX(k))    
    
#%%
plt.figure()
for k in range (1,7):
    plt.subplot(3,2,k)
    plt.title(u'Diagramme no ' + str(k))
    for l in {0.5, 1, 2}:
        plt.plot(dataX(k),dataY(k,l))
plt.show()

#%%
plt.figure()
X=np.linspace(-10,10,1000)
plt.plot(X, scs.norm().pdf(X))
plt.plot(X, scs.cauchy().pdf(X))

#%%
X=np.linspace(-5,5,1000)
plt.figure()
for l in {0.5, 1, 0.25,0.1,0.05}:
        plt.plot(X,scs.norm(0,l).pdf(X))
plt.show()
plt.figure()
for l in {0.5, 1, 0.25,0.1,0.05}:
        plt.plot(X,scs.norm(0,l).cdf(X))
plt.show()

#%%
plt.figure()
for k in range(0,8):
    plt.plot(dataX(5),scs.gamma(2**k,scale = 1/2**k).pdf(dataX(5)))
plt.show