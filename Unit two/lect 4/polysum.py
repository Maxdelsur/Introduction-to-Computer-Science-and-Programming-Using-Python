# -*- coding: utf-8 -*-
"""
Created on Tue Feb 23 08:20:15 2021

@author: Maxi
"""
def polysum(n,s):
    '''
    n: number of sides of a polygon
    s: length of each side
    
    This function should sum the area and square of the perimeter of the regular polygon. 
    The function returns the sum, rounded to 4 decimal places.
    '''
    from math import tan, pi
    area = (0.25*n*(s**2))/(tan(pi/n))
    perimeter = (s*n)**2
    return round(area+perimeter,4)
