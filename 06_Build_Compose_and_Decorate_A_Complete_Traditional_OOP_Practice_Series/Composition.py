class Engine:
    def start(self):
        print("🔧 Engine started... Vroom Vroom!")


class Car:
    def __init__(self, model, engine):
        self.model = model
        self.engine = engine  # Composition: Engine is part of Car

    def drive(self):
        print(f"🚗 {self.model} is ready to drive.")
        self.engine.start()


# Engine object
my_engine = Engine()

# Car object with Engine passed inside
my_car = Car("Toyota Corolla", my_engine)

# Access Engine's method via Car
print("\n" + "=" * 40)
print("          CAR SYSTEM STARTING")
print("=" * 40 + "\n")
my_car.drive()
