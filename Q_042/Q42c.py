# Write a program which can map() and filter() to make a list 
# whose elements are square of even number in [1,2,3,4,5,6,7,8,9,10].

def even(item):
    if item % 2 == 0:
        return item**2


lst = [i for i in range(1, 11)]
print(list(filter(lambda j: j is not None, list(map(even, lst)))))