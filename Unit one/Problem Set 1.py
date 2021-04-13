# -*- coding: utf-8 -*-
"""
Created on Sun Feb 28 11:37:04 2021

@author: Maxi
"""
# Problem 1
"""
Assume s is a string of lower case characters.

Write a program that counts up the number of vowels contained in the string s. Valid vowels are: 'a', 'e', 'i', 'o', and 'u'. For example, if s = 'azcbobobegghakl', your program should print:

"""
numVowels = 0
s = 'asdsagfvjdcsa'
for char in range(0,len(s)):
    if s[char] == 'a' or s[char] == 'e' or s[char] == 'i' or s[char] == 'o' or s[char] == 'u':
        numVowels += 1
    else:
        numVowels += 0
print("Number of vowels: ",numVowels)


# Problem 2
"""
Assume s is a string of lower case characters.

Write a program that prints the number of times the string 'bob' occurs in s. For example, if s = 'azcbobobegghakl', then your program should print

"""
s = 'azcbobobegghaklbobob' 
n=0 
for i in range(1,len(s)-1): 
    if s[i-1] == 'b' and s[i] == 'o' and s[i+1] == 'b': 
        n += 1 
    else: n+=0
print('Number of times bob occurs is: ' + str(n))

# Problem 3
"""
Assume s is a string of lower case characters.

Write a program that prints the longest substring of s in which the letters occur in alphabetical order. For example, if s = 'azcbobobegghakl', then your program should print

Longest substring in alphabetical order is: beggh

In the case of ties, print the first substring. For example, if s = 'abcbcd', then your program should print

Longest substring in alphabetical order is: abc

"""

s = 'azcd'
now = ""
ans = ""
for n in range(len(s)):
    if n+1 < len(s):
        if s[n] <= s[n+1]:
            now = now + s[n:n+1]
        else:
            now = now + s[n]
            if len(ans) < len(now):
                ans = now
                now = ""
            else:
                now = ""
    elif n+1 == len(s):
        if s[n] > s[n-1]:
            now = now + s[n]
if len(now) > len(ans):
    ans = now
    print("Longest substring in alphabetical order is:",ans)
else:
    print("Longest substring in alphabetical order is:",ans)