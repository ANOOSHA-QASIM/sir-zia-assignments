class A:
    def show(self):
        print("A's show")

class B(A):
    def show(self):
        print("B's show")

class C(A):
    def show(self):
        print("C's show")

class D(B, C):
    pass  # D inherits from B and C

d = D()
d.show()  # Calls show() following MRO

# Print MRO
for cls in D.__mro__:
    print(cls.__name__)
