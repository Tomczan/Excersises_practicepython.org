# https://www.practicepython.org/exercise/2014/03/12/06-string-lists.html

slowo = input("Podaj slowo, by sprawdzic czy jest palindromem: ")


if slowo == slowo[::-1]:
    print("Slowo jest palindromem")
else:
    print("Slowo nie jest palindromem")

