# Write a program to compute:

# f(n)=f(n-1)+100 when n>0
# and f(0)=0
# with a given n input by console (n>0).

# Example: If the following n is given as input to the program:

# 5
# Then, the output of the program should be:

# 500

n = int(input())
f = lambda x: f(x-1)+100 if x > 0 else 0
print(f(n))