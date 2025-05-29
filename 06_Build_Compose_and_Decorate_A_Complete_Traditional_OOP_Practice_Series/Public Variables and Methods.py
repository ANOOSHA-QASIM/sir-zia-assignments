class Car:
    def __init__(self , brand):
        self.brand = brand

    def start(self):
        print(f"{self.brand} is starting...")

my_car = Car("Toyota")
print("\n" + "=" * 40)
print("🚗 CAR INFORMATION 🚗".center(40))

print(my_car.brand)
my_car.start()
    
class Mobile:
    def __init__(self, model):
        self.model = model

    def call(self):
        print(f"{self.model} is making a call...\n")

my_mobile = Mobile("Samsung Galaxy")
print('\n' + '=' * 40)
print("📱 MOBILE INFORMATION 📱".center(40))
print(my_mobile.model)
my_mobile.call()

