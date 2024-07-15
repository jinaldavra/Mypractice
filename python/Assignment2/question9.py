# 9. Create a program that keeps asking the user for numbers until they enter a negative number, and then 
#    prints the sum of all entered numbers.


sum = 0

while(1):
    num = int(input("Enter the number : "))

    if num < 0:
        break

    sum += num

print(f"Total sum of all number is {sum}")



