# -*- coding: utf-8 -*-
"""
Created on Tue Feb  2 13:29:01 2021

Class on Strings

@author: Maxi
"""

# Starting with strings
hi = "Hello there"
greetings = "hello"
name = "Eric"
print(hi+" "+name)


# Print string Example
x = 1
print(x)
x_str = str(x)
print("my fav num is", x, ".", "x =", x)
print("my fav num is " + x_str + ". " + "x = " + x_str) # removes space between each element.

# Operations with strings - concatenate strings
"ab"+"cd" # concatenate
3*"eric" # sucesive concatenation
len("eric") # length
"eric"[1]   # indexing
"eric"[1:3] # slicing


str1 = 'hello'
str2 = ','
str3 = 'world'
str4 = str1 + str3

str4[:-1]
str4[::-1]

#The three numbers in a string slice are

#Start (inclusive) - defaults to start of string

#End (exclusive) - defaults to end of string

#Step - defaults to 1

#When you see [ : : -1 ], the empty spaces mean that the default values are used. So the slice here is the whole string, start to end, with a step of -1, so it counts backwards.
#"helloworld" becomes "dlrowolleh".


# input/output

text = input("Type anything... ")
print(5*text)

num = int(input("Type a number... "))
print(5*num)

# Exercises from strings

if 6 > 7:
   print("Yep")
#------

if 6 > 7:
   print("Yep")
else:
   print("Nope")
   

#----
var = 'Panda'
if var == "panda":
   print("Cute!")
elif var == "Panda":
   print("Regal!")
else:
   print("Ugly...")
   
#
temp = 120
if temp > 85:
   print("Hot")
elif temp > 100:
   print("REALLY HOT!")
elif temp > 60:
   print("Comfortable") 
else:
   print("Cold")
   
#
temp = 50
if temp > 85:
   print("Hot")
elif temp > 100:
   print("REALLY HOT!")
elif temp > 60:
   print("Comfortable")
else:
   print("Cold")