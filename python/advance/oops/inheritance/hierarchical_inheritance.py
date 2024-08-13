class A:
    def a(self):
        print("Class A method a()")

class B(A):
    def b(self):
        print("Class B method b()")

class C(A):
    def c(self):
        print("Class C method c()")

class D(B,C):
    def d(self):
        print("Class D method d()")

obj_of_d = D()
print(D.__mro__)
# print(D.mro())

obj_of_d.a()
obj_of_d.b()
obj_of_d.c()
obj_of_d.d()

# print(dir(D))

