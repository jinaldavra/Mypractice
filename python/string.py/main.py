# Creating a string with characters

# string length :

# string = len("Hello, world!")
# print(string)

# string type :

# string = type("Hello, world!")
# print(string)

# Indexing(+/-): Accessing individual characters in a string using their index position.

# string = "Hello, world!"[0]
# string = "Hello,world!"[1]
# string = "Hello,world!"[2]
# string = "Hello,world!"[3]
# string = "Hello,world!"[4]
# string = "Hello,world!"[5]
# string = "Hello,world!"[6]
# string = "Hello,world!"[7]
# string = "Hello,world!"[8]
# string = "Hello,world!"[9]
# string = "Hello,world!"[10]
# string = "Hello,world!"[11]

# string = "Hello,world!"[-1]
# string = "Hello,world!"[-2]
# string = "Hello,world!"[-3]
# string = "Hello,world!"[-4]
# string = "Hello,world!"[-5]
# string = "Hello,world!"[-6]
# string = "Hello,world!"[-7]
# string = "Hello,world!"[-8]
# string = "Hello,world!"[-9]
# string = "Hello,world!"[-10]
# string = "Hello,world!"[-11]
# string = "Hello,world!"[-12]
# print(string)

# Slicing(+/-): Extracting a portion of a string using a range of index positions.

# string = "Hello, world!"[0:13]
# string = "Hello, world!"[0:1]
# string = "Hello, world!"[0:2]
# string = "Hello, world!"[0:3]
# string = "Hello, world!"[0:4]
# string = "Hello, world!"[0:5]
# string = "Hello, world!"[0:6]
# string = "Hello, world!"[0:7]
# string = "Hello, world!"[0:8]
# string = "Hello, world!"[0:9]
# string = "Hello, world!"[0:10]
# string = "Hello, world!"[0:11]
# string = "Hello, world!"[0:12]
# string = "Hello, world!"[0:13]

# string = "Hello, world!"[0:5:2]
# string = "Hello, world!"[0:13:2]
# string = "Hello, world!"[0:13:5]

# string = "Hello, world!"[-1:]
# string = "Hello, world!"[-2:]
# string = "Hello, world!"[-3:]
# string = "Hello, world!"[-4:]
# string = "Hello, world!"[-5:]
# string = "Hello, world!"[-6:]
# string = "Hello, world!"[-7:]
# string = "Hello, world!"[-8:]
# string = "Hello, world!"[-9:]
# string = "Hello, world!"[-10:]
# string = "Hello, world!"[-11:]
# string = "Hello, world!"[-12:]
# string = "Hello, world!"[-13:]
# print(string)

# Concatenation: Combining two or more strings into a single string using the '+' operator.

# string1 = "Hello"
# string2 = "World"                      # without space
# add = string1 + string2
# print(add)

# string1 = "Hello"
# string2 = " "                            
# string3 = "World"                      # with space     
# add = string1 + string2 + string3
# print(add)

# string replica :

# string = "Hello, world !" * 3
# print(string)

# string methods :

# print(dir("string"))

# name = "PYTHON PROGRAMMING"
# print(name.lower())

# name = "python programming"
# print(name.upper())

# print(name.capitalize())

# print(name.title())

# print(name.swapcase())

# print(name.replace("python","java"))
# print(name.replace("programming","course"))

# title = "python programming" 
# print(len(title))     
  
# print(title.center(25))
# print(title.center(25,"-"))

# title1 = "        python programming        " 
# print(title1.strip())
# print(title1.lstrip())
# print(title1.rstrip())

# password = "jinal@1234"
# print(password.isalnum())

# digits = "1234567"
# print(digits.isdigit())

# char = "abcdef"
# print(char.isalpha())

# name = "jinaldavariya"
# print(name.islower())

# name = "JINALDAVARIYA"
# print(name.isupper())

# string = "I am a girl"
# print(string.isascii())
# print(string.isdecimal())
# print(string.isidentifier())
# print(string.isnumeric())
# print(string.isprintable())
# print(string.isspace())
# print(string.istitle())
# print(string.casefold())

# String formatting: Inserting variables into a string using the format() function or f-string syntax.

name = "jinal"
age = 22

# print("My name is {} and i am {} year old".format(name,age))

# print("My name is {0} and i am {1} year old".format(name,age))

# print(f"My name is {name} and i am {age} year old")

# print("My name is %s and i am %d year old" %(name,age))


# String formatting with precision and decimal places :

# print("{:.2f}".format(3.141767866) )


# String formatting with alignment and padding :

# print("{:^20}".format("Hello, world !"))

# print("{:>20}".format("Hello, world !"))

# print("{:<20}".format("Hello, world !"))

otp = "12345"
print(f"Your otp is : {otp}")






