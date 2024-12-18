# Please write a program to print the running time of execution of "1+1" for 100 times.

import time

before = time.time()
for i in range(100):
    x = 1 + 1
after = time.time()
execution_time = after - before
print(execution_time)