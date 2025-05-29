def double(num: int):
    return num * 2  # Multiply by 2

def triple(num: int):
    return num * 3  # Multiply by 3

def main():
    print("\n🚀 Welcome to the Doubling & Tripling Challenge!\n")
    
    num = int(input("🔢 Enter a number: "))  # User input
    
    num_times_2 = double(num)  # Get double
    num_times_3 = triple(num)  # Get triple
    
    # Show results
    print("\n✨ Results:")
    print(f"➡️  Double of {num} is 👉 {num_times_2}")
    print(f"➡️  Triple of {num} is 👉 {num_times_3}")
    
    print("\n🏁 Challenge Complete! 🎯\n")

if __name__ == '__main__':
    main()  # Run program
