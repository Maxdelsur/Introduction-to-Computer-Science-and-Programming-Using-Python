# -*- coding: utf-8 -*-
"""
Created on Wed Feb  3 10:46:02 2021

While and For loops

@author: Maxi
"""

# Example 1
n = input("You are in the Lost Forest. Go left or right? ")
while n == "right":
    n = input("You are in the Lost Forest. Go left or right? ")
print("You got out of the Lost Forest!")

#######
# Example 2

n = 0  # set something
while n < 5:  #while with condition
    print(n)  # True code
    n = n+1   # False Code
    
# Same with for loop

for n in range(5):
    print(n)

#######
# Example 3

mysum = 0
for i in range(7, 10):
    mysum += i
print(mysum)
    
mysum = 0
for i in range(5, 11, 2):
    mysum += i
print(mysum)

# example with break 

mysum = 0
for i in range(5, 11, 2):
    mysum += i
    if mysum == 5:
        break
print(mysum)



    

