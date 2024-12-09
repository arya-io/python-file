# Define a function which can generate a list 
# where the values are square of numbers between 1 and 20 (both included). 
# Then the function needs to print the last 5 elements in the list.

def squares(n):
    squares_list = [i**2 for i in range(1,n+1)]
    print(squares_list[-5:])
squares(20)