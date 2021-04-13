# https://www.practicepython.org/exercise/2014/04/25/12-list-ends.html

a = [5, 10, 15, 20, 25]

def first_and_last_element_of_list(listOne):
    return [listOne[0], listOne.pop()]

b = first_and_last_element_of_list(a)
    
print(b)
