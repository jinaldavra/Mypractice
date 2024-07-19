# Accessing elements from a dictionary :

contact = {
    'John doe' : '123-456-7890',
    'Jane doe' : '234-567-4560',
    'Alice johnson' : '777-777-7777',
}

# Accessing the value of a key  : 

# print(contact['Alice johnson'])
# print(contact['Jane doe'])
# print(contact['John doe'])

# print(dir(contact))

# 'clear', 'copy', 'fromkeys', 'get', 'items', 'keys', 'pop', 'popitem', 'setdefault', 'update', 
# 'values'

product = {
    'items' : ['tomato','potato']
}

# add key and values : 

# product['fruit'] = ['apple','banana']
# print(product)

# fromkeys : it print the same value in all key

# items = ['tomato','potato','onion']
# price = 30
# print(product.fromkeys(items,price))

# create an empty dictionary :

# product = dict()
# print(product)

car = {
    'brand' : 'bugatti',
    'model' : 'x10',
    'year'  : '2024',
    'colour': 'black',
    'doors' : '2',
    'transmission' : 'automatic',
    'fuel type' : 'electical',
}

# get value of given keys :

# print(car.get('brand'))
# print(car.get('model'))
# print(car.get('year'))
# print(car.get('colour'))
# print(car.get('doors'))
# print(car.get('transmission'))
# print(car.get('fuel type'))

# print only value :
# print(car.values())

# print only keys :
# print(car.keys())

# print all values and all keys :
# print(car.items())

# pop : remove given key
# car.pop('doors')
# car.pop('model')
# car.pop('transmission')
# car.pop('brand')
# car.pop('year')
# car.pop('colour')
# car.pop('fuel type')
# print(car)

# popitem : remove last key and value
# car.popitem()
# print(car)

# setdefault : add another key and value
# car.setdefault('speed','200')
# print(car)

# update : update key and value
# new_car = {
#     'price' : 30,
# }
# car.update(new_car)
# print(car)

# print all key and value using for loop:
# for key in car.keys():
#     print(key,car[key])

# print only values using for loop:
# for value in car.values():
#     print(value)

# print only keys using for loop:
# for key in car.keys():
#     print(key)

for key,value in car.items():
    print(key,value)