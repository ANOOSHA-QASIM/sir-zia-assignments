class Dog:
    def __init__(self, name, breed):
        self.name = name
        self.breed = breed

    def bark(self):
        print(f"{self.name} is barking! 🐶")

# Create dog object
dog1 = Dog("Bruno", "Labrador")

# Clean output
print("\n" + "=" * 40)
print("Name  :", dog1.name)
print("Breed :", dog1.breed)
dog1.bark()
print("=" * 40 + "\n")


