# 3. Write a program to compute the factorial of a number (input from the user) using a for loop.

num = int(input("Enter the number : "))
fact = 1

for num in range(1,num + 1):
    fact *= num

print(f"The factoiral of {num} is {fact}")
