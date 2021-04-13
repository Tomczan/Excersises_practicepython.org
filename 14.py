# https://www.practicepython.org/solution/2014/05/21/14-list-remove-duplicates-solutions.html

a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]

def remove_dup_loop(numbers_list):
    insideList = []
    for i in numbers_list:
        if i not in insideList:
            insideList.append(i)
    return insideList

def remove_dup_sets(numbers_list):
    return list(set(numbers_list))

x = remove_dup_loop(a)
y = remove_dup_sets(a)
print(x)
print(y)
