# Overriding method :

# class Parent:
#     def greet(self):
#         print("Hello from parent.")

# class Child(Parent):
#     def greet(self):
#         super().greet()
#         print("Hello from child.")

# obj_of_child = Child()
# obj_of_child.greet()

class Shape:
    def Name(self):
        print("Name of shape")

class Circle(Shape):
    def Name(self):
        super().Name()
        print("Circle")

class Square(Shape):
    def Name(self):
        super().Name()
        print("Square")

# obj_of_circle = Circle()
# obj_of_circle.Name()

obj_of_square = Square()
obj_of_square.Name()