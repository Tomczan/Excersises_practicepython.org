# https://www.practicepython.org/exercise/2014/02/26/04-divisors.html

number = int(input("Podaj liczbe: "))

i = list(range(1, number))
print(i)
print(type(i))
for item in i:
    if number % item == 0:
        print(item)

test = [item for item in i if (number % item == 0)]     


print(test)
print(type(test))
