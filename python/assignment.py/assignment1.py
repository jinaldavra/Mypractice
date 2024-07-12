# 1. Write a Python program to calculate the area of a rectangle given its length and width.

# length = 10
# width = 10

# Area = length * width
# print(f"Area of rectangle is {Area}")

# 2. Write a Python program that compares two integers and prints whether the first integer is greater, 
#    less than, or equal to the second integer.

# num1 = int(input("Enter the first integer  :"))
# num2 = int(input("Enter the second integer :"))

# if num1 > num2:
#     print(f"{num1} is greater than {num2}")
# elif num1 < num2:
#     print(f"{num1} is less than {num2}")
# else:
#     print(f"{num1} is equal to {num2}")

# 3. Write a Python program to swap two variables without using a temporary variable.

# var1 = 30
# var2 = 40

# var1,var2 = var2,var1
# print(var1,var2)

# 4. Write a Python program to check if a number is between 1 and 10 (inclusive).

# num = int(input("Enter the number : "))

# if 1 <= num <= 10:
#     print(f"{num} is between 1 and 10")
# else:
#     print(f"{num} is not between 1 and 10")

# 5. Write a Python program to perform bitwise AND, OR, and XOR operations on two integers.

# num1 = 10
# num2 = 4

# bitwise_and = num1 & num2
# print(bitwise_and)

# bitwise_or = num1 | num2
# print(bitwise_or)

# bitwise_xor = num1 ^ num2
# print(bitwise_xor)

# 6. Write a Python program that checks if a number is positive, negative, or zero.

# num = int(input("Enter the number : "))

# if num > 0:
#     print(f"{num} is positive number.")
# elif num < 0:
#     print(f"{num} is negative number")
# else:
#     print(f"{num} is zero")

# 7. Write a Python program that checks if a number is even or odd.

# num = int(input("Enter the number : "))

# if num % 2 == 0:
#     print(f"{num} is even number")
# else:
#     print(f"{num} is odd number")

# 8. Write a Python program that determines if a student's grade is 'A', 'B', 'C', 'D', or 'F' based on 
#    their score.

# score = int(input("Enter the score : "))

# if score >= 90:
#     print("A")
# elif score >= 80:
#     print("B")
# elif score >= 70:
#     print("C")
# elif score >= 60:
#     print("D")
# else:
#     print("F")

# 9. Write a Python program that checks if a number is divisible by both 3 and 5, divisible only by 3, 
#    divisible only by 5, or not divisible by either.

# num = int(input("Enter the number : "))

# if num % 3 == 0 and num % 5 == 0:
#     print(f"{num} is divisible by 3 and 5")
# elif num % 3 == 0:
#     print(f"{num} is only divisible by 3")
# elif num % 5 == 0:
#     print(f"{num} is only divisible by 5")
# else:
#     print("Not divisible by either 3 or 5")

# 10. Write a Python program that checks if a year is a leap year. A leap year is divisible by 4, but not
#     divisible by 100 unless it is also divisible by 400.

year = int(input("Enter the year : "))

if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
    print(f"{year} is a leap year")
else:
    print(f"{year} is not a leap year")


    













