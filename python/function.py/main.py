# def add_numbers(num1,num2):
#     print(num1 + num2)

# add_numbers(10,20)
# add_numbers(30,40)

# function to calculate the sum of two numbers :

# def sum_of_numbers(a,b):
#     return a + b

# result = sum_of_numbers(10,20)
# print(result)


# function to calculate the multiply of two numbers :

# def multi_of_numbers(a,b):
#     return a * b

# result = multi_of_numbers(10,5)
# print(result)


# function to calculate the sub of two numbers :

# def sub_of_numbers(a,b):
#     return a - b

# result = sub_of_numbers(20,10)
# print(result)


# function to calculate the div of two numbers :

# def div_of_numbers(a,b):
#     return a // b

# result = div_of_numbers(10,5)
# print(result)


# types of arguments :

# 1] positional arguments
# 2] default/keyword arguments
# 3] variable length arguments

# def add_numbers(a,b,c):
#     print(a + b + c)

# add_numbers(10,20,30)

# def bill(tomato = 120,potato = 80):
#     return tomato + potato

# print(bill())
# print(bill(20))


# *args - value :

# def add_numbers(*nums):
#     # print(type(nums))
#     print(sum(nums))

# add_numbers(10,20,30,40,50)

# **kwargs - key-value

# def bill(**products):
#     total = 0
#     for product, price in products.items():
#         print(f"{product} : {price}")
#         total += price
#     print("-------------------------------")
#     return f"Total amount is : {total}"

# print(bill(tomato = 100,potato = 200, book = 30,pen = 20))


# function scope :

# x = 20

# def test():
#     global x   # using global keyword to modify the value of x
#     x = 10
#     print(x)

# test()
# print(x)

# lambda function :

# cube = lambda x : x*x*x
# print(cube(3))


# map function :

# num = [1,2,3,4,5]
# square = lambda x : x*x
# print(list(map(square,num)))

# example of map function :

# def even_odd(num):
#     if num % 2 == 0:
#         return 'even'
#     else:
#         return 'odd'
# numbers = [1,2,3,4,5,6]
# output = list(map(even_odd,numbers))
# print(output)

        #    or

# def even_odd(num):
#     if num % 2 == 0:
#         return 'even'
#     else:
#         return 'odd'
# numbers = [1,2,3,4,5,6]
# output = [even_odd(num) for num in numbers]
# print(output)

# filter function :

# print even number using filter :

# def is_even(num):
#     return num % 2 == 0

# numbers = [1,2,3,4,5,6,7,8]
# even_numbers = list(filter(is_even,numbers))
# print(even_numbers)

# print odd number using filter : 

# def is_odd(num):
#     return num % 2 != 0

# numbers = [1,2,3,4,5,6,7,8]
# odd_numbers = list(filter(is_odd,numbers))
# print(odd_numbers)

# outer function & inner function :

# def outer_function():
#     def inner_function():
#         return "from inner function"
#     return inner_function()
# print(outer_function()) 

# decorators :

def upper_case(func):
    def wrapper():
        result= func()
        return result.upper()
    return wrapper
@upper_case
def test():
    return input("Enter something.....")
print(test())