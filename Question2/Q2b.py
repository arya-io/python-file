# Write a program which can compute the factorial of a given numbers.
# The results should be printed in a comma-separated sequence on a single line.
# Suppose the following input is supplied to the program: 8 Then, the output should be:40320

# Using While Loop

n = int(input()) #input() function takes input as string type
                 #int() converts it to integer type
fact = 1
i = 1
while i <= n:
    fact = fact * i
    i = i + 1
print(fact)