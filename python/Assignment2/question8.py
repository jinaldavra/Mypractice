# 8. Generate a multiplication table for numbers 1 to 10 using nested loops.

num = int(input("Enter the number : "))

start = 1
for i in range(1,11):
    if start <= 10:
        print(num,start,num*start)
        start+= 1
    else:
        print(i)
        

# for i in range(1,11):
#     for j in range(1,11):
#         print(f"{i * j : 3}",end = "")
#     print()



    