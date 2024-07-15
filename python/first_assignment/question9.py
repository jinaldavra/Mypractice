# 9. Write a Python program that checks if a number is divisible by both 3 and 5, divisible only by 3, 
#    divisible only by 5, or not divisible by either.

num = int(input("Enter the number : "))

if num % 3 == 0 and num % 5 == 0:
    print(f"{num} is divisible by 3 and 5")
elif num % 3 == 0:
    print(f"{num} is only divisible by 3")
elif num % 5 == 0:
    print(f"{num} is only divisible by 5")
else:
    print("Not divisible by either 3 or 5")