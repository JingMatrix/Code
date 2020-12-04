# -*- coding: utf-8 -*-
"""
Created on Mon Jan 13 17:32:50 2020

@author: JingMatrix
"""

import numpy as np
import matplotlib.pyplot as plt
import scipy.stats as scs


Fission = np.loadtxt('TP1_Fission.txt')
print('The size of data is:')
print(len(Fission))
print('\nThe mean value of data is:')
print(np.mean(Fission))
print('\nThe varation of data is:')
print(np.var(Fission))
print('\nThe standard deviation of data is:')
print(np.std(Fission))
print('\nThe first quantile of data is:')
print(np.quantile(Fission, 0.25))
print('\nThe third quantile of data is:')
print(np.quantile(Fission,0.75))
print('\nThe interquartile range of data is:')
print(np.quantile(Fission,0.75)-np.quantile(Fission,0.25))
print('\nThe maximum of data is:')
print(np.max(Fission))
print('\nThe minimum of data is:')
print(np.min(Fission))

#%%
X=np.linspace(0,np.max(Fission),1000)
loi_empirique=scs.rv_discrete
plt.figure()
plt.subplot(2,1,1)
plt.hist(Fission,bins = 30,density = True)
#plt.plot(X,scs.expon(scale = np.mean(Fission)).pdf(X))
plt.subplot(2,1,2)
plt.step(np.sort(Fission),np.arange(0,1,1./len(Fission)))
#plt.plot(X,scs.expon(scale = np.mean(Fission)).cdf(X))
plt.show

#%%
X=np.linspace(0,np.max(Fission),1000)
loi_empirique=scs.rv_discrete
plt.figure()
plt.subplot(2,1,1)
plt.hist(Fission,bins = 30,density = True)
plt.plot(X,scs.expon(scale = np.mean(Fission)).pdf(X))
plt.subplot(2,1,2)
plt.step(np.sort(Fission),np.arange(0,1,1./len(Fission)))
#plt.plot(X,ECDF(Fission)(X))
#plt.plot(X,scs.expon(scale = np.mean(Fission)).cdf(X))
plt.show
