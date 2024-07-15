# 14. Create a list of squares for numbers from 1 to 20 using a loop.

square = [None] * 20

for i in range(1,21):
    square[i-1] = i ** 2
    
print(square)
