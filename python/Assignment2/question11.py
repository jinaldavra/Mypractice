# 11. Generate the Fibonacci sequence up to the nth term (where n is provided by the user) using a loop.

num = int(input("Enter the number : "))

a,b = 0,1

for i in range(num):
    print(a,end = " ")
    a, b = b, a + b