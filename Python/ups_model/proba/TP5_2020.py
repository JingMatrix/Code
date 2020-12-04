# -*- coding: utf-8 -*-

import matplotlib.pyplot as plt
import numpy as np
import scipy.stats as scs
from scipy.linalg import toeplitz



#%%%%%%%%%%%%%%
### Donnees Nil

Nil = np.loadtxt('Nil.txt')
X = Nil[:,1]
plt.figure()
plt.plot(Nil[:,0],X)
plt.title("Donnees Nil")

Xbar = np.mean(X)
n = len(X)-1

#%% Donnees Nil, correlogramme

K=30

rhat = np.zeros(K+1)
for k in range(K+1):
    rhat[k] = np.mean((X[k:]-Xbar)*(X[:n-k+1]-Xbar))
rhohat = rhat/rhat[0]

plt.figure()
plt.scatter(range(K+1),rhohat)
plt.title("correlogramme Nil")

#%% Donnees Nil, test, p-values
# n = len(X)
Tn = np.sqrt(n)*np.abs(rhohat[1:])
pval = 2*scs.norm.sf(Tn)
print("p-values for k=0,...,30:\n ", pval)


  #%% Donnees Nil, trace de Y

Y = np.cumsum(X-Xbar)
plt.figure()
plt.plot(Nil[:,0],Y)
plt.title("trace de $Y$")

#%% Donnees Nil, variation quadratique
    
def varQuad(Y,a):
    n = len(Y)-1
    m = int(n/a)-1
    V = np.zeros(m)
    for t in range(m):
        V[t] = (Y[a*(t+2)]-2*Y[a*(t+1)]+Y[a*t])**2
    return np.mean(V)

#%% Donnees Nil, estimateur de H

S = [varQuad(Y,a) for a in range(1,K+1)]
plt.figure()
plt.loglog(range(1,K+1),S)
plt.title("loglog plot of $S_n(a)$")
print("estimator for H: ",np.polyfit(np.log(range(1,K+1)),np.log(S),1)[0]/2)

#%% simulation, definitions

def r(k,H):
    return 0.5*(np.abs(k+1)**(2*H)+np.abs(k-1)**(2*H)  - 2*np.abs(k)**(2*H))

def simFracNoiseSlow(n,H):
    C=np.zeros(shape=(n+1,n+1))
    for i in range(n+1):
        for j in range(n+1):
            C[i,j]=r(i-j,H)
    L = np.linalg.cholesky(C)
    return np.dot(L,scs.norm.rvs(size=n+1))

def simFracNoise(n,H):
    C = toeplitz(r(np.arange(n+1),H))
    L = np.linalg.cholesky(C)
    return np.dot(L,scs.norm.rvs(size=n+1))


    
#%% simulation et tracés
n=1000

plt.figure()
for (i,H) in zip(range(1,5),[0.5,0.65,0.8,0.95]):
    X = simFracNoise(n,H)
    Y = np.cumsum(X)

    plt.subplot(2,4,i)
    plt.plot(X)
    plt.subplot(2,4,4+i)
    plt.plot(Y)
    plt.title("$H="+str(H)+"$")
    

#%% estimateur de H

n=1000
H=0.8
X = simFracNoise(n,H)
Y = np.cumsum(X)

S = [varQuad(Y,a) for a in range(1,K+1)]
plt.figure()
plt.loglog(range(1,K+1),S)
plt.title("loglog plot of $S_n(a)$")
print("estimator for H: ",np.polyfit(np.log(range(1,K+1)),np.log(S),1)[0]/2,
      ", real value: ",H)

#%% TCL pour S_n(a) (attention, long avec la fonction simFracNoiseSlow!)

a = 2
n = 300
M = 5000
H = 0.9
S = np.zeros(M)
for m in range(M):
    X = simFracNoise(n,H)
    Y = np.cumsum(X)
    S[m] = varQuad(Y,a)
    
Snorm = np.sqrt(n)*(S - (4-2**(2*H))* a**(2*H))
#Snorm = Snorm/np.std(Snorm)
l = np.arange(-100,101)
gamma = a**(4*H+1)/2*np.sum(
    (np.abs(l+2)**(2*H)
     +np.abs(l-2)**(2*H)
     -4*np.abs(l+1)**(2*H)
     -4*np.abs(l-1)**(2*H)
     +6*np.abs(l)**(2*H))**2)
Snorm=Snorm/np.sqrt(gamma)
plt.figure()
plt.hist(Snorm,bins=30,density=True)
x = np.linspace(-3,3,100)
plt.plot(x,scs.norm.pdf(x))
plt.figure()
plt.plot(np.sort(Snorm),np.arange(0,1,1/len(S)))
plt.plot(x,scs.norm.cdf(x))

