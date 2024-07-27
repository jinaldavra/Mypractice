# Dictionary Iteration:
# 7. Write a Python program to iterate over a dictionary and print all keys and values.

car = {
    'name' : 'bugatti',
    'model' : 'x10',
    'year' : '2010',
    'speed' : 'automatic',
    'doors' : '2',
}

for key,values in car.items():
    print(key,values)