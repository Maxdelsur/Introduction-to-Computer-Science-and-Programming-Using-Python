# -*- coding: utf-8 -*-
"""
Created on Fri Feb 19 13:06:34 2021

@author: Maxi
"""
str1 = 'exterminate!' 
str2 = 'number one - the larch'

str2.swapcase()
str2.capitalize()
type(str1.index('e'))
str2.index('n')
str2.find('n')
str2.index('!')
str2.find('!')
str1.index('!')
str1.find('!')
str1.count('e')
str1 = str1.replace('e', '*')
str1
str2.replace('one', 'seven')
str2 = str2.capitalize()
str2
str2.swapcase()
str2.find('n')
str2.replace('one', 'seven')
def odd(x):
    '''
    x: int

    returns: True if x is odd, False otherwise
    '''
    # Your code here
    return x%2!=0

odd(1)
odd(2)
odd(3)
odd(8)
