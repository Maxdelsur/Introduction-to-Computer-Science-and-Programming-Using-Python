# -*- coding: utf-8 -*-
"""
Created on Sun Feb 21 12:32:01 2021

@author: Maxi
"""
## ITERATION VERSUS RECURSION

# iterative
def iterPower(base, exp):
    '''
    base: int or float.
    exp: int >= 0
 
    returns: int or float, base^exp
    '''
    # Your code here
    result = 1
    for i in range(1,exp+1):
        result *= base
    return result

iterPower(2, 2)

## recursive Power function
def recurPower(base, exp):
    '''
    base: int or float.
    exp: int >= 0
 
    returns: int or float, base^exp
    '''
    # Your code here
    if exp == 0:
        return 1
    elif exp == 1:
        return base
    else: 
        exp = exp-1
        return base*recurPower(base,exp)

recurPower(3, 3)


### HANOI TOWERS

def printMove(fr, to):
    print('move from ' + str(fr) + ' to ' + str(to))

def Towers(n, fr, to, spare):
    if n == 1:
        printMove(fr, to)
    else:
        Towers(n-1, fr, spare, to)
        Towers(1, fr, to, spare)
        Towers(n-1, spare, to, fr)

print(Towers(4, 'P1', 'P2', 'P3'))


### Greatest common divisor
## ITERATIVE
def gcdIter(a, b):
    '''
    a, b: positive integers
    
    returns: a positive integer, the greatest common divisor of a & b.
    '''
    # Your code here
    divisor = a
    while divisor > 0:
        if a%divisor != 0 or b%divisor !=0:
            divisor -=1
        else:
           return divisor
    
gcdIter(9, 12)

### RECURSIVE

def gcdRecur(a, b):
    '''
    a, b: positive integers
    
    returns: a positive integer, the greatest common divisor of a & b.
    '''
    # Your code here
    divisor = 7
    if b == 0:
        divisor = a
    elif a%divisor == 0 and b%divisor == 0:
        divisor = divisor
    else:
        divisor = gcdRecur(b, a%b)
    return divisor
        
gcdRecur(6,12)


# ANSWER
def gcdRecur(a, b):
    '''
    a, b: positive integers
    
    returns: a positive integer, the greatest common divisor of a & b.
    '''
    # Base case is when b = 0
    if b == 0:
        return a

    # Recursive case
    return gcdRecur(b, a % b)



## RECURSIVE WITH MULTIPLE CASES: FIBONACCI
    
### as we have two recursive functions, we need to base cases to refer
def fib(x):
    """assumes x an int >= 0
       returns Fibonacci of x"""
    if x == 0 or x == 1:
        return 1
    else:
        return fib(x-1) + fib(x-2)

fib(7)

## Recursion on non-numerical

## DIVIDE AND CONQUER ALGORITHM - Subproblem solution!



def isPalindrome(s):

    def toChars(s):
        s = s.lower()
        ans = ''
        for c in s:
            if c in 'abcdefghijklmnopqrstuvwxyz':
                ans = ans + c
        return ans

    def isPal(s):
        if len(s) <= 1:
            return True
        else:
            return s[0] == s[-1] and isPal(s[1:-1])

    return isPal(toChars(s))

print("")
print('Is eve a palindrome?')
print(isPalindrome('eve'))

print('')
print('Is able was I ere I saw Elba a palindrome?')
print(isPalindrome('Able was I, ere I saw Elba'))


### EXERCISE
def isIn(char, aStr):
    '''
    char: a single character
    aStr: an alphabetized string
    
    returns: True if char is in aStr; False otherwise
    '''
    # Your code here
    low = 0
    high = len(aStr)
    ans = int((high+low)/2)
    def sortchar(aStr):
        s= sorted(aStr)
        aStr= "".join(s)
        return aStr
    
    if char==sortchar(aStr)[ans]:
        return char==sortchar(aStr)[ans]
    elif char<sortchar(aStr)[ans]:
        high = ans
        ans = int((high+low)/2)
        aStr = aStr[:high]
    else: 
        low = ans
        ans = int((high+low)/2)
        aStr = aStr[low:]
    return isIn(char,aStr)

isIn("e","vevo")


### EXERCISE
## My Answer
def isIn(char, aStr):
    '''
    char: a single character
    aStr: an alphabetized string
    
    returns: True if char is in aStr; False otherwise
    '''
    # Your code here
    def sortchar(aStr):
        s= sorted(aStr)
        aStr= "".join(s)
        return aStr
    low = 0
    high = len(aStr)
    ans = int((high+low)/2)
    aStr = sortchar(aStr)

    if len(aStr) == 0:
        return False
    elif len(aStr)==1:
        return char==aStr
    elif char < aStr[ans]:
        aStr = aStr[:(high-1)]
    else:
        aStr = aStr[ans:]
    return isIn(char,aStr)

isIn("e","vdsnkfsdjhgjnlkmnkmmkgflkgf")

## MIT ANSWER
def isIn(char, aStr):
   '''
   char: a single character
   aStr: an alphabetized string
   
   returns: True if char is in aStr; False otherwise
   '''
   # Base case: If aStr is empty, we did not find the char.
   if aStr == '':
      return False

   # Base case: if aStr is of length 1, just see if the chars are equal
   if len(aStr) == 1:
      return aStr == char

   # Base case: See if the character in the middle of aStr equals the 
   #   test character 
   midIndex = len(aStr)//2
   midChar = aStr[midIndex]
   if char == midChar:
      # We found the character!
      return True
   
   # Recursive case: If the test character is smaller than the middle 
   #  character, recursively search on the first half of aStr
   elif char < midChar:
      return isIn(char, aStr[:midIndex])

   # Otherwise the test character is larger than the middle character,
   #  so recursively search on the last half of aStr
   else:
      return isIn(char, aStr[midIndex+1:])



## Exercise polygon

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


            
    
    




