"""Ask the user for a number. Depending on whether the number is even or odd, print out an
appropriate message to the user. Hint: how does an even / odd number react differently when
divided by 2?

Extras:

If the number is a multiple of 4, print out a different message.
Ask the user for two numbers: one number to check (call it num) and one number to divide by (check).
If check divides evenly into num, tell that to the user.
If not, print a different appropriate message.
"""

def guess_number(guessing_number):
    print(guessing_number * 4)
    while True:
        number = int(input("Put a number, guess the number: "))
        if (number < guessing_number):
            print("Number is lower that the number, guess again")
        elif (number == guessing_number * 4):
            print("This number is 4 times bigger than guessing number.")    
        elif (number > guessing_number):
            print("Number is higher than the number, guess again.")
        elif (number == guessing_number):
            print("Congratulation, you guessed the number!")
            break
    
guess_number(4)
