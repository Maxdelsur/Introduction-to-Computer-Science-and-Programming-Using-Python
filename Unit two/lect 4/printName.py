# -*- coding: utf-8 -*-
"""
Created on Mon Jun 13 15:14:30 2016

@author: ericgrimson
"""

def printName(firstName, lastName, reverse =False):
    if reverse:
        print(lastName + ', ' + firstName)
    else:
        print(firstName, lastName)
        
        
printName("Max","DelSur")
printName("Max","DelSur", True)
