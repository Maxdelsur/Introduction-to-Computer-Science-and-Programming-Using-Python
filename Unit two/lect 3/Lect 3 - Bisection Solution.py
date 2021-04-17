# -*- coding: utf-8 -*-
"""
Created on Wed Feb 17 19:56:11 2021

@author: Maxi
"""
### Bisection Search
### sqrt bisection
x = 25
epsilon = 0.001
numGuesses = 0
low = 0.0
high = x
ans = (high + low)/2.0

while abs(ans**2 - x) >= epsilon:
    print('low = ' + str(low) + ' high = ' + str(high) + ' ans = ' + str(ans))
    numGuesses += 1
    if ans**2 < x:
        low = ans
    else:
        high = ans
    ans = (high + low)/2.0
print('numGuesses = ' + str(numGuesses))
print(str(ans) + ' is close to square root of ' + str(x))




cube = 27
epsilon = 0.01
num_guesses = 0
low = 0
high = cube
guess = (high + low)/2.0
while abs(guess**3 - cube) >= epsilon:
    if guess**3 < cube :
        low = guess
    else:
        high = guess
    guess = (high + low)/2.0
    num_guesses += 1
print('num_guesses =', num_guesses)
print(guess, 'is close to the cube root of', cube)


#challenges  modify to work with negative cubes!
# modify to work with x < 1!

### My code exercise: Guess my number

low = 0
high = 100
ans = (high+low)/2
my_input = "e"
print("Please think of a number between 0 and 100!")

while my_input != "c":
    print("Is your secret number {0:.0f}?".format(ans))
    my_input = input("Enter 'h' to indicate the guess is too high. Enter 'l' to indicate the guess is too low. Enter 'c' to indicate I guessed correctly: ")
    if my_input != "c" and my_input  !="h" and my_input != "l":
        print("Sorry, I did not understand your input")
    elif my_input == "h":
        high = ans
        ans = int((high+low)/2)
    elif my_input == "l":
        low = ans
        ans = int((high+low)/2)
    else:
        print("Game over. Your secret number was: {0:.0f}".format(ans))
        
        