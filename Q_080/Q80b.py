# Please write a program to print the list after removing even numbers in [5,6,77,45,22,12,24].

def isEven(n):
    return n%2!=0

li = [5,6,77,45,22,12,24]
lst = list(filter(isEven,li))
print(lst)