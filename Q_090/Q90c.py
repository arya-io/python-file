# Please write a program which count and print the numbers of each character in a string input by console.

# Example: If the following string is given as input to the program:

# abcdefgabc
# Then, the output of the program should be:

# a,2
# c,2
# b,2
# e,1
# d,1
# g,1
# f,1

s = input()
for letter in range(ord('a'),ord('z')+1):    # ord() gets the ascii value of a char
    letter = chr(letter)                     # chr() gets the char of an ascii value
    cnt = s.count(letter)
    if cnt > 0:
        print("{},{}".format(letter,cnt))