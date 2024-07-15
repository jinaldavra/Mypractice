# 4. Write a Python program to check if a number is between 1 and 10 (inclusive).

num = int(input("Enter the number : "))

if 1 <= num <= 10:
    print(f"{num} is between 1 and 10")
else:
    print(f"{num} is not between 1 and 10")