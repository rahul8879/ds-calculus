# -*- coding: utf-8 -*-
"""
Created on Wed Dec  7 09:26:26 2022

@author: Rahul
"""
#how to code functions in numpy and sympy 
#how to plot function in a set domain
#How to convert sympy expression into numpy format.

import numpy as np
from sympy import *
import matplotlib.pyplot as plt


#defining the domain
resolution = .1
x = np.arange(-2,2.1,resolution)

#print(max(domain))
#lets write the symbol


y = x**2 + 3*x**3 -x**4




    


    
plt.plot(x,y,label = 'y = x**2 + 3*x**3 -x**4')
plt.grid()
plt.legend()
plt.xlim(-2, 2)
plt.xlabel("X")
plt.ylabel("Y")
plt.show()
    
    
    

