# String Case Conversion:
# 17. Write a Python program to convert all lowercase characters to uppercase and vice versa in a string.

string = input("Enter the string : ")
converted_string = ''

for ch in string:
    if ch.islower():
        converted_string += ch.upper()
    elif ch.isupper():
       converted_string += ch.lower()
    else:
        converted_string += ch

print(f"Converted string is {converted_string}")


