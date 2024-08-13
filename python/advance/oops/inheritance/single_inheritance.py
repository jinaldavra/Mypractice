class A:
    def a(self):
        print("Class A method a()")

class B(A):
    def b(self):
        print("Class B method b()")

obj_of_b = B()
obj_of_b.a()
obj_of_b.b()

print(dir(B))
    