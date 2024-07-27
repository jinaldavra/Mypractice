# List Sorting:
# 2. Write a Python program to sort a list of tuples based on the second item.

list = [(2,7),(1,3),(2,5),(4,2)]

list.sort(key=lambda x:x[1])
print(list)