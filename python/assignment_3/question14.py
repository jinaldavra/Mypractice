# Dictionary Update:
# 14. Write a Python program to update the value of a specific key in a dictionary.

dict = {
    'car' : 'Bugatti',
    'model' : 'x10',
    'year' : '2010',
    'doors' : '2',
}

new_dict = {
    'colour' : 'black'
}
dict.update(new_dict)
print(dict)
