# Please write a program to output a random even number between 0 and 10 inclusive using random module and list comprehension.

li = [2,4,6,8]
import random
print(random.choice([i for i in range(11) if i%2==0]))