# -*- coding: utf-8 -*-
"""
Created on Tue Feb  2 12:40:52 2021

@author: Maxi
"""
# Some Basic Commands
x = 5
print(type(x))

pi_approx = 22/7
radius = 2.2
area = pi_approx*(radius**2)
radius = radius +1

print("The area of the circle is {}". format(float(area)))



## if - else basics
x = int(input('Enter an integer: '))
if x%2 == 0:    ##Test
    print('')   ## block
    print('Even') ##block
else:
    print('')  #False Block
    print('Odd') #False Block
print('Done with conditional')  # rest 

# Python uses identation to identify each part of the code


### Nested Conditonals

if x%2 == 0:
    if x%3 == 0:
        print('Divisible by 2 and 3')
    else:
        print('Divisible by 2 and not by 3')
elif x%3 == 0:
    print('Divisible by 3 and not by 2')

### Compound Booleans --> Sequence of tests

x=2
y=3
z=4

if x < y and x < z:
    print ('x is least')
elif y<z:
    print('y is least')
else: 
    print ("z is least")
