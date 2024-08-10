# class Maths:
#     # data member
#     num1 = 20
#     num2 = 10
#     # methods
#     def add(self):
#         print(self.num1 + self.num2)
#     def sub(self):
#         print(self.num1 - self.num2)
#     def multi(self):
#         print(self.num1 * self.num2)
#     def div(self):
#         print(self.num1 // self.num2)

# obj = Maths()
# obj.add()
# obj.sub()
# obj.multi()
# obj.div()
# print(obj.num1)
# print(obj.num2)

# class Auth:
#     class Register:
#         def __init__(self, username, email, password, confirm_password):
#             self.username = username
#             self.email = email
#             self.password = password
#             self.confirm_password = confirm_password

#         def validate_username(self):
#             if len(self.username) < 8:
#                 return False
#             if not self.username.isalnum():
#                 return False
#             return True
        
#         def validate_email(self):
#             if "@" not in self.email or "." not in self.email:
#                 return False
#             return True
        
#         def validate_password(self):
#             if len(self.password) < 8:
#                 return False
#             if not self.password.isalnum():
#                 return False
#             if self.password != self.confirm_password:
#                 return False
#             return True

#         def register(self):
#             if self.validate_username() and self.validate_email() and self.validate_password():
#                 print("Registration successfull !")
#             else:
#                 print("Registration failed.")

#     class login:
#         def __init__(self, username, password):
#             self.username = username
#             self.password = password

#         def login_authentification(self):
#             if self.username == "admin123" and self.password == "password":
#                 print("Login successfull !")
#             else:
#                 print("Login failed.")

# auth = Auth()

# register_obj = auth.Register("admin123", "admin@gmail.com", "password", "password")
# register_obj.register()

# register_user_1 = auth.Register("admin1234", "admin124@gmail.com", "password", "password") 
# register_user_1.register()

# login_obj = auth.login("admin123", "password")
# login_obj.login_authentification()

# while(1):
#     username = input("Enter username : ")
#     password = input("Enter password : ")
#     login_user_1 = auth.login(username,password)
#     login_user_1.login_authentification()


class Auth:
    class Register:
        def __init__(self, username, email, password, confirm_password):
            self.username = username
            self.email = email
            self.password = password
            self.confirm_password = confirm_password

        def validate_username(self):
            if len(self.username) < 8:
                return False
            if self.username.isalnum():
                return False
            return True
        
        def validate_email(self):
            if "@" not in self.email or "." not in self.email:
                return False
            return True
        
        def validate_password(self):
            if len(self.password) < 8:
                return False
            if self.password.isalnum():
                return False
            if self.password != self.confirm_password:
                return False
            return True

        def register(self):
            if self.validate_username() and self.validate_email() and self.validate_password():
                print("Registration successfull.")
            else:
                print("Registration failed.")

    class login:
        def __init__(self, username, password):
            self.username = username
            self.password = password

        def login_authentification(self):
            if self.username == "admin123" and self.password == "password":
                print("Login successfull.")
            else:
                print("Login failed.")

auth = Auth()

register_obj = auth.Register("admin123","admin123@gmail.com","password","password")
register_obj.register()

login_user_1 = auth.login("admin123","password")
login_user_1.login_authentification()



                
            

    
        
    
            

