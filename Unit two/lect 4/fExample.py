# -*- coding: utf-8 -*-
"""
Created on Fri Jun 10 12:59:05 2016

@author: ericgrimson
"""
## Understanding the scope of a function
#####


def f( x ):
    #x = 7
    x = x + 1
    print('in f(x): x =', x)
    return x
x = 3
z = f( x )
