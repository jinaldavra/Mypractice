# 2. Write a Python program that compares two integers and prints whether the first integer is greater, 
#    less than, or equal to the second integer.

num1 = int(input("Enter the first integer  :"))
num2 = int(input("Enter the second integer :"))

if num1 > num2:
    print(f"{num1} is greater than {num2}")
elif num1 < num2:
    print(f"{num1} is less than {num2}")
else:
    print(f"{num1} is equal to {num2}")