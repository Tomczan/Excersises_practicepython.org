# https://www.practicepython.org/exercise/2014/04/30/13-fibonacci.html

def fib(arg):
    a, b = 0, 1
    print("1 :",a)
    print("2 :",b)
    for i in range(2, arg+1):
        a, b = b, a + b
        print(i,":",b)

x = int(input("How many fibonacci numbers do you want to print "))
fib(x)

    
        
    
