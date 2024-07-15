# 15. Write a program to print the following pattern: "right-angled triangle star pattern"

# * 
# * * 
# * * * 
# * * * * 
# * * * * *

rows = 5

for i in range(1,rows + 1):
    for j in range(1,i + 1):
        print("*",end = " ")
    print()