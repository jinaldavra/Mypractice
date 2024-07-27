# List Concatenation:
# 15. Write a Python program to concatenate multiple lists.

list1 = [1,2,3,4,5]
list2 = [6,7,8]
list3 = [9,10]

list1.extend(list2)
list1.extend(list3)
print(list1)