# https://www.practicepython.org/exercise/2014/04/02/09-guessing-game-one.html

import random


def guess_number():
    randomNumber = random.randint(1,9)
    print(randomNumber)
    i = 0
    while True:
        i += 1
        userInput = input("Guess a number in range 1 - 9, type break if you want finish ")
        if userInput == 'break':
            return False
        else:
            userInput = int(userInput)
            if userInput >= 10:
                print("Number out of range, guess again")            
                continue
            elif userInput == randomNumber:                
                return i
            elif userInput > randomNumber:              
                print("Number is too high")
                continue
            elif userInput < randomNumber:             
                print("Number is too low")
                continue

guess = guess_number()
if(guess == False):
    print("You stopped a program")
else:    
    print("You guessed in number", guess,"tries")
