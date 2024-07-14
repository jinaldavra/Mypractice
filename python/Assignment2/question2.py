# 2. Create a program that calculates the sum of the first 100 natural numbers using a while loop.

start = 1
sum = 0

while start <= 100:
    sum += start
    start+= 1

print(f"The sum of the first 100 natural numbers is {sum}")