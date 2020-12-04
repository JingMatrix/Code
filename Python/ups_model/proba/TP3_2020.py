# -*- coding: utf-8 -*-

import numpy as np
import matplotlib.pyplot as plt
import scipy.stats as scs


#%% Exo 1, LFGN, avec Unif.
    
N = 10000 #Nombre de tirages
plt.figure()
for i in range(5):
    X=scs.uniform.rvs(size=N)
    moyenneEmp= np.cumsum(X)/np.arange(1,N+1) 
    plt.subplot(2,1,1)
    plt.axhline(0.5, color="black")
    plt.plot(np.arange(1,N+1), moyenneEmp)
    plt.subplot(2,1,2)
    plt.plot(np.log10(np.arange(1,N+1)), moyenneEmp)
    plt.axhline(0.5, color="black")
plt.show()


#%% Exo 1, LFGN, avec Cauchy : pas de convergence p.s cette fois, car X non intégrable (espérance n'est pas définie)

#Affichage
plt.figure()
for i in range(5):
    Z=scs.cauchy.rvs(size=N) 
    moyenneEmp=np.cumsum(Z)/np.arange(1,N+1) 
    plt.subplot(2,1,1)
    plt.plot(np.arange(1,N+1) ,moyenneEmp)
    plt.axhline(0, color="black")
    plt.subplot(2,1,2)
    plt.plot(np.log10(np.arange(1,N+1)), moyenneEmp)
    plt.axhline(0, color="black")
plt.show()




#%% Exo 2.3, fonction Polya

def Polya(N):
    U = np.random.random_sample(N)
    X = np.zeros(N+1)
    X[0]=1
    for n in range(N):
        X[n+1] = X[n] + (U[n]<=X[n]/(n+2))
    return X

    
#%% Exo 2.4, tracés de trajectoires
    
N = 1000
    
plt.figure()
for i in range(5):
    plt.plot(Polya(N)/np.arange(2,N+3))
plt.show()


#%% Exo 2.5, fonction Polya2

def Polya2(N,a,b):
    U = np.random.random_sample(N)
    X = np.zeros(N+1)
    X[0]=a
    for n in range(N):
        X[n+1] = X[n] + (U[n]<=X[n]/(n+a+b))
    return X


#%% Exo 2.5, tracés de trajectoires
    
N = 1000
    
plt.figure()
for i in range(5):
    plt.plot(Polya2(N,2,3)/np.arange(2,N+3))
plt.show()

#%% Exo 2.5, fonction de répartition empirique de la proportion limite
   
M = 1000
N = 100
sample=np.zeros((M,N+1))
for i in range(M):
    sample[i]=Polya2(N,2,3)
plt.figure()
for n in [25,50,100]:
    plt.step(np.sort(sample[:,n]/(n+5)),np.arange(0,1,1/M))
plt.show()


#%% Ex 3.4 Fct de répartition empirique


def DistanceToUnif(sample):
    sortedsample = np.sort(sample)
    n = len(sample)
    return max(np.max(np.arange(1,n+1)/n - sortedsample),
                  np.max(sortedsample - np.arange(n)/n))
    
#%% Ex 3.5

N = 5000
X = np.random.random_sample(N)
D = [DistanceToUnif(X[:n+1]) for n in range(N)]
    
plt.figure()
plt.plot(range(1,N+1),D)
plt.axhline()
plt.show()

# commentaires:
# Le trace suggère que la distance entre \hat F_n et F tend vers 0, mais plutôt
# lentement. Un seul tracé ne suffit à priori pas, car il serait possible que
# la convergence vers 0 n'ait lieu qu'avec une certaine probabilité non nulle
# mais différente de 1. Il faut donc répéter plusieurs fois l'expérience afin
# de conclure qu'il s'agit d'un événement de probabilité égale à ou proche de
# 1.
# Ceci dit, à cause de la loi du 0-1 de Kolmogorov, on voit rapidement que
# la probabilité de cette événement doit être égale à 0 ou 1, donc en réalité
# il suffirait un seul ou un petit nombre de tracés.

#%% Ex 3.6

M = 1000
Z1 = [np.sqrt(25)*DistanceToUnif(np.random.random_sample(25)) for m in range(M)]
Z2 = [np.sqrt(50)*DistanceToUnif(np.random.random_sample(50)) for m in range(M)]
Z3 = [np.sqrt(100)*DistanceToUnif(np.random.random_sample(100)) for m in range(M)]

plt.figure()
plt.step(np.sort(Z1),np.arange(0,1,1/M))
plt.step(np.sort(Z2),np.arange(0,1,1/M))
plt.step(np.sort(Z3),np.arange(0,1,1/M))
plt.show()

 
#%% Exo 4, loi exponentielle

plt.figure()
X = np.linspace(-3,3,1000)
for n in [10,40,160]:
    plt.plot(X,scs.gamma.pdf(X,n,loc=-np.sqrt(n),scale=1/np.sqrt(n)))
plt.plot(X,scs.norm.pdf(X))
plt.show()
plt.figure()
for n in [10,40,160]:
    plt.plot(X,scs.gamma.cdf(X,n,loc=-np.sqrt(n),scale=1/np.sqrt(n)))
plt.plot(X,scs.norm.cdf(X))
plt.show()


D = [np.max(np.abs(scs.gamma.cdf(X,n,loc=-np.sqrt(n),scale=1/np.sqrt(n))
 - scs.norm.cdf(X))) for n in range(1,201)]

plt.figure()
plt.subplot(1,2,1)
plt.plot(range(1,201),D)
plt.subplot(1,2,2)
plt.loglog(range(1,201),D)
plt.show()

print(D[99]/D[199])
print(np.sqrt(2))
C = np.sqrt(200) * D[199]
print("équivalent asymptotique: ",C,"x n^(-1/2)")

