# https://www.practicepython.org/exercise/2014/04/16/11-check-primality-functions.html

import math

def is_prime(number):
    if number < 2:
        return False
    for x in range(2,int(math.sqrt(number)+1)):
        if number % x == 0:
            return False
    return True


for x in range (0,100):
    print(x,":",is_prime(x))




