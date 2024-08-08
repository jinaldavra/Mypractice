# create file :

file_name = "sample.txt"

# file = open(file_name,'w')

file = open(file_name, 'r')

# print(file.tell())

# print(file.seek(7))
# print(file.tell())

# print(file.read())

# file = open(file_name, 'x')


#  write data into the file :

# data = "My name is jinal"
# file.write(data)

lines = [
    'This is a line - 1\n',
    'This is a line - 2\n',
    'This is a line - 3\n',
    'This is a line - 4\n',
    'This is a line - 5\n',
]
# file.writelines(lines)


# read data from the file :

# print(file.read(6))
# print(file.read())


# print(file.readline())
# print(file.readline())
# print(file.readline())
# print(file.readline())
# print(file.readline())

# print(file.readlines())

# file.close()

# print(file.read())

# import os
# import uuid


# file_name = f"{str(uuid.uuid4())}.txt"

# os.system(f'type nul > {file_name}')

# os.system('py test.py')

# os.remove(r'E:\PYTHON\advance\file_handling\e413a7c1-6a0c-4089-92b8-c9b7c1b8e9f2.txt')

# os.rename('req.txt',f"{str(uuid.uuid4())}.txt")

with open(r'E:\PYTHON\advance\file_handling\sample.txt','r')  as file:
    data = file.read()
    print(data)





