# -*- coding: utf-8 -*-
"""
Created on Wed Feb  3 12:14:24 2021

@author: Maxi
"""

# Example - Iterative Multiplication

x = 3  # 1)iteration variable outside the loop
ans = 0 # 2)change variable within the loop

itersLeft = x # 3) test variable to test when done
while (itersLeft != 0):
    ans = ans + x  #2)
    itersLeft = itersLeft - 1
print(str(x) + '*' + str(x) + ' = ' + str(ans))

#This code squares the value of x by repetitive addition


## Examples of Loops

num = 989415
for num in range(5):
    print(num)
print(num)

divisor = 2
for num in range(0, 10, 2):
    print(num/divisor) 
    

for variable in range(20):
    if variable % 4 == 0:
        print(variable)
    if variable % 16 == 0:
        print('Foo!') 
        
        
#######
for letter in 'hola':
    print(letter)  
######
count = 0
for letter in 'Snow!':
    print('Letter # ' + str(count) + ' is ' + str(letter))
    count += 1
    break
print(count)

#####
myStr = '6.00x'

for char in myStr:
    print(char)

print('done')


####

greeting = 'Hello!'
count = 0

for letter in greeting:
    count += 1
    if count % 2 == 0:
        print(letter)
    print(letter)

print('done')


####
school = 'Massachusetts Institute of Technology'
numVowels = 0
numCons = 0

for char in school:
    if char == 'a' or char == 'e' or char == 'i' \
       or char == 'o' or char == 'u':
        numVowels += 1
    elif char == 'o' or char == 'M':
        print(char)
    else:
        numCons -= 1

print('numVowels is: ' + str(numVowels))
print('numCons is: ' + str(numCons)) 


#### cube guess-and-check method

x = int(input('Enter an integer: '))
ans = 0
while ans**3 < x:
    ans = ans + 1
if ans**3 != x:
    print(str(x) + ' is not a perfect cube')
else:
    print('Cube root of ' + str(x) + ' is ' + str(ans))


# modified

x = int(input('Enter an integer: '))
ans = 0
while ans**3 < abs(x):
    ans = ans + 1
if ans**3 != abs(x):
    print(str(x) + ' is not a perfect cube')
else:
    if x < 0:
        ans = - ans
    print('Cube root of ' + str(x) + ' is ' + str(ans))
    
    
# for version -->  it doesn't break
cube = 28
for guess in range(cube+1):
    if guess**3 == cube:
        print("Cube root of ", cube, " is ", guess)

# negative test version
cube = -288
for guess in range(abs(cube)+1):
    if guess**3 >= abs(cube):
        break
if guess**3 != abs(cube):
    print(cube, "is not a perfect cube")
else:
    if cube < 0:
        guess = -guess
        print('Cube root of ' + str(cube) + ' is ' + str(guess))


### problem 1

s = 'azcbobobegghakl'
count=0
for i in range(0,len(s)):
    if s[i] in ("a","e","i","o","u"):
        count+=1
    else: 
        count+=0
print("Number of Vowels: "+str(count))
        
#### Problem 2
s = 'azcbobobegghaklbobob' 
n=0 
for i in range(1,len(s)-1): 
    if s[i-1] == 'b' and s[i] == 'o' and s[i+1] == 'b': 
        n += 1 
    else: n+=0
print('Number of times bob occurs is: ' + str(n))

### problem 3      
               
s = 'azcbobobegghakl'
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
    
    
    
