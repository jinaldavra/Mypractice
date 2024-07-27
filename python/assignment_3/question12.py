# Nested List:
# 12. Write a Python program to flatten a nested list.

list = [[1],[2,3],[4,5,6],[7,8]]

flatten_list = [num for sublist in list for num in sublist] 

print(flatten_list)

