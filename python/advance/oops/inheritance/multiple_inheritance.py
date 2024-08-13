class A:
    def a(self):
        print("Class A method a()")

class B:
    def b(self):
        print("Class B method b()")

class C(A,B):
    def c(self):
        print("Class C method c()")

obj_of_c = C()
obj_of_c.a()
obj_of_c.b()
obj_of_c.c()

print(dir(C))

