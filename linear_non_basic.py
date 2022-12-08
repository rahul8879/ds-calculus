# -*- coding: utf-8 -*-
"""
Created on Wed Dec  7 09:26:26 2022

@author: Rahul
"""
#how to code functions in numpy and sympy 
#how to plot function in a set domain
#How to convert sympy expression into numpy format.

import numpy as np

import sympy as sym
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


#create a symbolic variable
beta = sym.var('beta')
#print(type(beta))

#define the function
s_y = beta**2 + 3*beta**3 -beta**4
print(s_y)
sym.plot(s_y,(beta,-2,2),xlabel='x',ylabel=None,title=f'${sym.latex(s_y)}$')
    
    
    

