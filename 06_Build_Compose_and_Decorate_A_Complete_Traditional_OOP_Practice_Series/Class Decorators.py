def add_greeting(cls):
    def greet(self):
        return "\nHello from Decorator!\n"
    cls.greet = greet
    return cls

@add_greeting
class Person:
    pass

p = Person()
print(p.greet())
