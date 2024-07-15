# 13. Write a program to find the largest number in a list using a loop.

list = [23,56,45,80,46,34]

if not list:
    largest_num = None
else:
    largest_num = list[0]

for i in list:
    if i > largest_num:
        largest_num = i

print(f"The largest number is {largest_num}")
