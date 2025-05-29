class Product:
    def __init__(self, price):
        self._price = price  # Private attribute

    @property
    def price(self):
        return self._price  # Get price

    @price.setter
    def price(self, new_price):
        if new_price >= 0:
            self._price = new_price  # Set price if valid
        else:
            print("⚠️  Price can't be negative!")  # Warn if invalid

    @price.deleter
    def price(self):
        print("🔔 Price is deleted\n")  
        del self._price  # Delete price

# Usage
print("=" * 40)
print("       PRODUCT PRICE DETAILS")
print("=" * 40)

p = Product(100)
print(f"Initial price: ${p.price}")

p.price = 150
print(f"Updated price: ${p.price}")

p.price = -50  # Invalid price

del p.price
