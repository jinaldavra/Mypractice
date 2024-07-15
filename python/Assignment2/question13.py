# 13. Write a program to find the largest number in a list using a loop.

num = [23,45,67,56,78,34,12]
max = 0

for i in num:
    if i > max:
        max = i
        
print(max)