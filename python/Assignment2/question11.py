# 11. Generate the Fibonacci sequence up to the nth term (where n is provided by the user) using a loop.

num = int(input("Enter the number : "))

a , b = 0,1
print(a,end = " ")
print(b,end=" ")

for i in range(num):
    num = a + b
    a = b
    b = num
    print(num,end=" ")
    
    
   