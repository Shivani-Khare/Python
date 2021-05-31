'''Program to let the user guess a number and output the appropiateness of the guessed number 
with the random number selected by the program.'''

print ("!!!----Guess Game----!!!")
import random                                        #Importing the library random from Python 
n = random.randrange(1,20)                           #Setting the range of the random number to be selected by the program 
guess_value = int(input("Enter your guess : "))

while n != guess_value:                              #Condition iterating loop
    if guess_value<n:
        print ("Your guess is too low from the original number")
        guess_value = int(input("Enter any other number as your guess : "))
    
    elif guess_value > n:
        print("Your guess is too high from the original value")
        guess_value = int(input("Enter any other number as your guess"))

    else:
        break

print ("Hurray!! Your guess is absolutely correct")