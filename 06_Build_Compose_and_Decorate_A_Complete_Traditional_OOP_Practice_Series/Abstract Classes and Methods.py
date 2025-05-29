from abc import ABC, abstractmethod

# Abstract base class
class Shape(ABC):
    @abstractmethod
    def area(self):
        pass

# Circle class
class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return 3.14 * self.radius ** 2

# Rectangle class
class Rectangle(Shape):
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def area(self):
        return self.length * self.width

# Triangle class
class Triangle(Shape):
    def __init__(self, base, height):
        self.base = base
        self.height = height

    def area(self):
        return 0.5 * self.base * self.height

# Create objects
circle = Circle(7)
rectangle = Rectangle(10, 5)
triangle = Triangle(6, 4)

# Display areas
print("\n" + "="*40)
print("          📏 SHAPE AREAS")
print("="*40)
print(f"🔵 Circle Area    : {circle.area()} sq units")
print(f"⬛ Rectangle Area : {rectangle.area()} sq units")
print(f"🔺 Triangle Area  : {triangle.area()} sq units")
print("\n" + "="*40)