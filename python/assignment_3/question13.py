# Dictionary Sorting:
# 13. Write a Python program to sort a dictionary by its values.

dict = {
    'B' : '2',
    'A' : '1',
    'D' : '4',
    'C' : '3',
}

new_dict = sorted(dict.items())
print(new_dict)