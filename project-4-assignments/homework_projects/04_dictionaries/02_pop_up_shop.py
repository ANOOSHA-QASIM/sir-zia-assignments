def main():
    # Welcome message with tip
    print("\n📖 Welcome to the Emoji Pop-Up Shop!")
    print("💡 Tip: You can update prices if items repeat.\n")

    # Fruit prices
    fruit_prices = {
        '🍎 Apple': 1.5,
        '🥭 Mango': 5,
        '🍌 Banana': 1
    }

    # User cart for storing quantities
    user_cart = {}

    # Ask for fruit quantities
    for fruit_name in fruit_prices:
        quantity = int(input(f"🛒 How many {fruit_name} do you want? "))
        user_cart[fruit_name] = quantity

    # Calculate total cost
    total_cost = 0

    # Print receipt
    print("\n🧾 Your Receipt:")
    for fruit_name in fruit_prices:
        quantity = user_cart[fruit_name]
        price = fruit_prices[fruit_name]
        print(f"➡️  {fruit_name} × {quantity} @ ${price} each = ${quantity * price}")
        total_cost += quantity * price

    # Show total cost
    print(f"\n💰 Total Cost: ${total_cost}")
    print("🛍️  Thank you for shopping with us! Come again!\n")

# Run the main function
if __name__ == "__main__":
    main()
