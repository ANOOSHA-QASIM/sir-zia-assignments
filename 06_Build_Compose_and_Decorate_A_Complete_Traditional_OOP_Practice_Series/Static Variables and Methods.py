class MathUtils:
    @staticmethod
    def add(a, b):
        return a + b

    @staticmethod
    def multiply(a, b):
        return a * b

result1 = MathUtils.add(5, 3)
print("\nAddition result:", result1, "\n")

result2 = MathUtils.multiply(4, 6)
print("Multiplication result:", result2, "\n")
