# -*- coding: utf-8 -*-
"""
Created on Tue Dec  6 21:57:15 2022

@author: Rahul
"""



#1/0 problem

from sympy import limit, Symbol

# function to calculate the limit of a function 
def test_v(input_1):
    #credit : https://bobbyhadz.com/blog/python-zerodivisionerror-float-division-by-zero
    #Different types of indeterminant forms : https://byjus.com/maths/indeterminate-forms/
    try:
    
        result = 1/(input_1-2)**2
        return result
    except ZeroDivisionError:
        x = Symbol('x')
        y=1/(x-2)**2

        result = limit(y, x, 0)
        
        return result
     

#test_v(1)
if __name__ == "__main__":
    print(test_v(2))