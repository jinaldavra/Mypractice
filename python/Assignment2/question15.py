# 15. Write a program to print the following pattern: "right-angled triangle star pattern"

# * 
# * * 
# * * * 
# * * * * 
# * * * * *

num = 5

for row in range(1,num + 1):
    for col in range(1,row + 1):
        print("*",end = " ")
    print()

