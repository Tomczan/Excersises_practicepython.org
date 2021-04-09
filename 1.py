""" https://www.practicepython.org/exercise/2014/01/29/01-character-input.html

Create a program that asks the user to enter their name
and their age. Print out a message addressed to
them that tells them the year that they will turn 100 years old.

Extras:

Add on to the previous program by asking the user for another number and printing out that many copies of the previous message.
(Hint: order of operations exists in Python)
Print out that many copies of the previous message on separate lines.
(Hint: the string "\n is the same as pressing the ENTER button)
"""
import datetime

def when_year_100(name, age, how_much = 1):
    for iteration in range(how_much):
        thisYear = int(datetime.date.today().strftime("%Y"))
        to100 = (100 - age) + thisYear
        print(name,", you will turn 100 years in ", to100, sep="") 
    return to100


name = input("What's your name? ")
age = int(input("What's your age? "))
how_much = int(input("How many times you want to print this message? "))
when_year_100(name, age, how_much)
