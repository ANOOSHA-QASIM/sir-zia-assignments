def main():
    print("\n✨ Welcome to the Subtraction Program! ✨\n")  # Starting message
    
    # User se number input lein
    num = int(input("🔢 Enter a number: "))
    
    # Subtract 3 aur result print karein
    result = subtract_three(num)
    
    # Result display
    print(f"\n🧮 The result after subtracting 3 is: {result}\n")
    
    print("✔️ Thank you for using the program! Have a great day! 😊\n")  # Ending message

def subtract_three(num):
    # 3 subtract kar ke return karein
    return num - 3

if __name__ == '__main__':
    main()
