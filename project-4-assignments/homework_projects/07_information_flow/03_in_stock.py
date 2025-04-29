def main():
    # User se fruit ka naam lena
    fruit = input("\n🍎 Enter the fruit name: ")
    
    # Stock check karna aur result print karna
    stock = num_in_stock(fruit)

    print("\n--- Result ---\n")  # Gap for clean output
    
    if stock == 0:
        print(f"❌ Sorry, {fruit} is out of stock.")
    else:
        print(f"✅ {fruit} is in stock. We have {stock} available.")

    print("\n--- End of Program ---\n")  # Gap for clean output

def num_in_stock(fruit: str) -> int:
    """Check the stock of the given fruit."""
    # Fruit aur unki stock quantities
    if fruit == "apple":
        return 10
    elif fruit == "banana":
        return 5
    elif fruit == "orange":
        return 0
    elif fruit == "grape":
        return 20
    elif fruit == "mango":
        return 15
    else:
        return 0

if __name__ == "__main__":
    main()
