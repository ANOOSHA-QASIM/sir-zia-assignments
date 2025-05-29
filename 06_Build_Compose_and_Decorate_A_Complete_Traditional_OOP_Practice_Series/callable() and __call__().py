class Multiplier:
    def __init__(self, factor):
        self.factor = factor  # factor set kiya

    def __call__(self, num):
        return num * self.factor  # multiply kar raha

mul = Multiplier(5)

print("\nCallable?", callable(mul))  # check callable hai ya nahi
print("mul(10) =", mul(10))        # object ko function ki tarah call kiya
print()
