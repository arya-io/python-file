# Write a program that accepts a sequence of whitespace separated words as input and 
# prints the words after removing all duplicate words and sorting them alphanumerically.

# Suppose the following input is supplied to the program:

# hello world and practice makes perfect and hello world again
# Then, the output should be:

# again and hello makes perfect practice world

inp_string = input("Enter string: ").split()
out_string = []
for words in inp_string:
    if words not in out_string:
        out_string.append(words)
print(" ".join(sorted(out_string)))