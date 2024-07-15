# 8. Generate a multiplication table for numbers 1 to 10 using nested loops.

for i in range(1,11):
    for j in range(1,11):
        print(f"{i * j : 3}",end = "")
    print()

    