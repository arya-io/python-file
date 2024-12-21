# Please write a program which prints all permutations of [1,2,3]

from itertools import permutations

def permutaion_generator(iterable):
    p = permutations(iterable)
    for i in p:
        print(i)

x = [1,2,3]
permutaion_generator(x)