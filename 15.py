# https://www.practicepython.org/exercise/2014/05/21/15-reverse-word-order.html

def reverse(string):
    result = string.split()
    revers = []
    for i in reversed(result):
        revers.append(i)
    return " ".join(revers)

sample = "My name is Michele"
print(reverse(sample))



    
