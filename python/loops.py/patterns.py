# 1 2 3 4 5
# 1 2 3 4 5
# 1 2 3 4 5
# 1 2 3 4 5
# 1 2 3 4 5

# num = 5

# for row in range(1,num+1):
#     for col in range(1,num+1):
#         print(col,end = " ")
#     print()

# 1 1 1 1 1
# 2 2 2 2 2
# 3 3 3 3 3
# 4 4 4 4 4
# 5 5 5 5 5

# num = 5
# for row in range(1,num+1):
#     for col in range(1,num+1):
#         print(row,end = " ")
#     print()

# 1
# 1 2
# 1 2 3
# 1 2 3 4
# 1 2 3 4 5

# num = 5

# for row in range(1,num+1):
#     for col in range(1,row+1):
#         print(col,end = " ")
#     print()

# 1
# 2 2
# 3 3 3
# 4 4 4 4
# 5 5 5 5 5

# num = 5

# for row in range(1,num+1):
#     for col in range(1,row+1):
#         print(row,end=" ")
#     print()

# 1
# 2 1
# 3 2 1
# 4 3 2 1
# 5 4 3 2 1

# num = 5

# for row in range(1,num+1):
#     for col in range(row,0,-1):
#         print(col,end=" ")
#     print()

# 5 4 3 2 1
# 4 3 2 1
# 3 2 1
# 2 1
# 1

# num = 5

# for row in range(1,num+1):
#     for col in range(num-row+1,0,-1):
#         print(col,end = " ")
#     print()

# * * * * *
# * * * *
# * * *
# * *
# *

# num = 5

# for row in range(1,num+1):
#     for col in range(num-row+1,0,-1):
#         print("*",end = " ")
#     print()

# E D C B A
# D C B A
# C B A
# B A
# A

# num = 5

# for row in range(num+1):
#     for col in range(num-row,0,-1):
#         print(chr(col+64),end=" ")
#     print()

# 1
# 2 3
# 4 5 6
# 7 8 9 10
# 11 12 13 14 15

# num = 5
# g = 1

# for row in range(1,num+1):
#     for col in range(row,0,-1):
#         print(g,end = " ")
#         g+=1
#     print()

# 1
#   2
#     3
#       4
#         5

# num = 5

# for row in range(1,num+1):
#     for col in range(1,num+1):
#         if row == col:
#             print(row,end=" ")
#         else:
#             print(" ",end = " ")
#     print()

# 1 2 3 4 5
# 6 7 8 9 10
# 11 12 13 14 15
# 16 17 18 19 20
# 21 22 23 24 25

# num = 5
# g = 1

# for row in range(1,num+1):
#     for col in range(1,num+1):
#         print(g,end=" ")
#         g+=1
#     print()

# 5 
# 5 4 
# 5 4 3 
# 5 4 3 2 
# 5 4 3 2 1

# num = 5

# for row in range(1,num+1):
#     for col in range(num,num-row,-1):
#         print(col,end=" ")
#     print()

#         1 
#       1 2 
#     1 2 3 
#   1 2 3 4 
# 1 2 3 4 5

num = 5

for row in range(1,num+1):
    for col in range(num,row,-1):
            print(" ",end=" ")
    for col in range(1,row+1):
            print(col,end=" ")
    print()




