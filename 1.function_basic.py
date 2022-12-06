# -*- coding: utf-8 -*-
"""
Created on Tue Dec  6 21:57:15 2022

@author: Rahul
"""



#1/0 problem



#learning resources : https://www.epythonguru.com/2019/12/how-to-compute-limit-in-python-using-sympy.html

from sympy import limit, Symbol
import logging



# function to calculate the limit of a function 
def test_v(input_1):
    #credit : https://bobbyhadz.com/blog/python-zerodivisionerror-float-division-by-zero
    #Different types of indeterminant forms : https://byjus.com/maths/indeterminate-forms/
    try:
        
        logging.debug('hey I am inside the try block')

        result = 1/(input_1**2-4)
        return result
    
    except ZeroDivisionError:
        logging.critical('hey I am from except block')

        x = Symbol('x')
        y=(x-2)/(x**2-4)

        result = limit(y, x, input_1)
        
        return result
     

#test_v(1)
if __name__ == "__main__":
    print(test_v(1))