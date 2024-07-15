# 6. Write a Python program that checks if a number is positive, negative, or zero.

num = int(input("Enter the number : "))

if num > 0:
    print(f"{num} is positive number.")
elif num < 0:
    print(f"{num} is negative number")
else:
    print(f"{num} is zero")