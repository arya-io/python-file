# By using list comprehension, please write a program to print the list after 
# removing the 0th, 2nd, 4th,6th numbers in [12,24,35,70,88,120,155].

orig_lst = [12,24,35,70,88,120,155]
indices = [0, 2, 4, 6]

new_list = [i for (j, i) in enumerate(orig_lst) if j not in indices]
print(new_list)