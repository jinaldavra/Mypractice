# 7. Write a program that takes a string input from the user and prints it in reverse using a for loop.

string = input("Enter the string : ")
rev_string = ""

for ch in string:
    rev_string = ch + rev_string

print(rev_string)
