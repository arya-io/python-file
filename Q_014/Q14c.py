# Write a program that accepts a sentence and calculate the number of upper case letters and lower case letters.

# Suppose the following input is supplied to the program:

# Hello world!
# Then, the output should be:

# UPPER CASE 1
# LOWER CASE 9

word = input()
upper,lower = 0,0

for i in word:
        lower+=i.islower()
        upper+=i.isupper()

print("UPPER CASE {0}\nLOWER CASE {1}".format(upper,lower))