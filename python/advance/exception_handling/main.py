# print("start")
# try:
#      b = int(input("Enter a number : "))
#      a = 10
#      print(a)
# except ZeroDivisionError:
#      print("Error : Division by zero is not allowed.")
# except ValueError:
#      print("Value error")
# except TypeError:
#      print("Type error")
# except NameError:
#      print("Name error")
# except Exception as err:
#     print("An error occured : ",err)
# else:
#      print(a + 20)
# finally:
#      print("This block is always execute.")
# print("end")

bal = 2000
with_balance = 20000

# if with_balance > bal:
#     raise ValueError("Insufficient balance")

assert (with_balance < bal), "Insufficient balance"
