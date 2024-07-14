# 5. Write a program that counts how many even and odd numbers are in a list.

list = [1,2,3,4,5,6]
odd_count = 0
even_count = 0

for i in list:
    if i % 2 == 0:
        even_count += 1
    else:
        odd_count += 1

print(f"The number of even number is {even_count}")
print(f"The number of odd number is {odd_count}")