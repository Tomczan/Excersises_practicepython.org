# https://www.practicepython.org/exercise/2014/04/10/10-list-overlap-comprehensions.html

import random

def two_lists_comprehension(listOne, listTwo):
    return list(set(listOne) & set(listTwo))

a = sorted(random.sample(range(30), random.randint(5,20)))
b = sorted(random.sample(range(30), random.randint(5,20)))


print("List a: {}".format(a))
print("List b: {}".format(b))
print("List contains only the elements that are commont between the lists: {}".format(sorted(two_lists_comprehension(a,b))))



