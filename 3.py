# https://www.practicepython.org/exercise/2014/02/15/03-list-less-than-ten.html

a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
b = []

number = int(input("Podaj liczbe: "))
'''
for item in a:
    if item < number:
        b.append(item)

print(b)        
'''

print([item for item in a if item < number])
