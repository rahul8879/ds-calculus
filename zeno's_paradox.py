# -*- coding: utf-8 -*-
"""
Created on Fri Dec  9 12:15:38 2022

@author: Rahul
"""

import numpy as np

def fxx(u):
    ot = (u**2-1)
    return ot

a = 2

x0 =np.array([a-1,a+1])
iterations = 10

xLimVals = np.zeros((iterations,2))
lmit_vals = np.zeros((iterations,2))

for i in range(iterations):
    
    xLimVals[i:,]   = x0
    
    lmit_vals[i:,] = fxx(x0)
    
    
    x0 = (x0+a)/2
    

print('limit from left')
print(np.stack((xLimVals[:,0],lmit_vals[:,0])).T)


print('limit from right')
print(np.stack((xLimVals[:,1],lmit_vals[:,1])).T)

print('Actual value at 2:',fxx(2))
    



