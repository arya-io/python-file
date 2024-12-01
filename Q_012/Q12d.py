# Write a program, which will find all such numbers between 1000 and 3000 (both included) such that 
# each digit of the number is an even number.
# The numbers obtained should be printed in a comma-separated sequence on a single line.

lst = [str(i) for i in range(1000,3001)]
lst = list(filter(lambda i:all(ord(j)%2 == 0 for j in i), lst))   # using lambda to define function inside filter function
print(",".join(lst))