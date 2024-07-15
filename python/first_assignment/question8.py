# 8. Write a Python program that determines if a student's grade is 'A', 'B', 'C', 'D', or 'F' based on 
#    their score.

score = int(input("Enter the score : "))

if score >= 90:
    print("A")
elif score >= 80:
    print("B")
elif score >= 70:
    print("C")
elif score >= 60:
    print("D")
else:
    print("F")