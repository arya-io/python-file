# Write a program which can map() and filter() to make a list 
# whose elements are square of even number in [1,2,3,4,5,6,7,8,9,10].

def even(x):
    return x%2==0

def square(x):
    return x*x

li = [1,2,3,4,5,6,7,8,9,10]
li = map(square,filter(even,li))   # first filters number by even number and the apply map() on the resultant elements
print(list(li))