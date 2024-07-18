# 11. Generate the Fibonacci sequence up to the nth term (where n is provided by the user) using a loop.

num = int(input("Enter the number : "))
n1 = 0
n2 = 1

for i in range(num):
    if i == 0:
        print(0,end=" ")
    elif i == 1:
        print(1,end=" ")
    else:
        nth = n1 + n2
        print(nth,end=" ")
        n1 = n2
        n2 = nth

# num = int(input("Enter the number : "))

# a , b = 0,1
# print(a,end = " ")
# print(b,end=" ")

# for i in range(num):
#     num = a + b
#     a = b
#     b = num
#     print(num,end=" ")
    
    
   