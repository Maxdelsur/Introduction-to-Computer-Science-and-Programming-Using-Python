# -*- coding: utf-8 -*-
"""
Created on Mon Apr 12 19:15:47 2021

@author: Maxi
"""
# Extras from Lect 2

# Write a piece of Python code that prints out the string 'hello world' if the value of an 
# integer variable, happy, is strictly greater than 2.+
happy = 5
if happy > 2:  #while with condition
    print("hello world")  # True code
    
# ver
num = 0
while num <= 5:
    print(num)
    num += 1

print("Outside of loop")
print(num) 

## Example of While loop
numberOfLoops = 0
numberOfApples = 2
while numberOfLoops < 10:
    numberOfApples *= 2
    numberOfApples += numberOfLoops
    numberOfLoops -= 1
print("Number of apples: " + str(numberOfApples))

## Example of While loop
num = 10
while num > 3:
    num -= 1
    print(num) 
    
    
## Example of While loop
num = 10
while True:
    if num < 7:
        print('Breaking out of loop')
        break
    print(num)
    num -= 1
print('Outside of loop')

## Example of While loop
num = 100
while not False:
    if num < 0:
        break
print('num is: ' + str(num)) 

## Example of While loop
num = 0
while num < 10:
    num += 2
    print(num)
print("Goodbye!")

## Example of While loop
print("Hello!")
num = 12
while num >= 4:
    num -= 2
    print(num)
    
## Example of While loop    
end = 5
while num < sum(range(end))+end:
    num = sum(range(end))+end
    print(num)
num = 0


# Here is one of a few ways to solve this problem:
total = 0
current = 1
while current <= end:
    total += current
    current += 1

print(total)


#
for i in range(2,12,2):
    print(i)
print("Goodbye!")

#
print("Hello!")
for i in range(10,0,-2):
    print(i)
    
# 
end = 6
total = 0
current = 1
for i in range(0, end):
    total += current
    current += 1
print (total)