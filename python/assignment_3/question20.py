# String Palindrome:
# 20. Write a Python program to check if a given string is a palindrome.

string = input("Enter the string : ")

cleaned_str = string.replace(" ","").lower()

is_palindrom = cleaned_str == cleaned_str[::-1]

if is_palindrom:
    print(f"{string} is a palindrom.")
else:
    print(f"{string} is not a palindrom.") 
