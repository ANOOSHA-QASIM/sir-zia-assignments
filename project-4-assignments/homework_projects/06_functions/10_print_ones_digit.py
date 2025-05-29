def print_ones_digit(num):
    # Print ones digit
    print("The ones digit is:", num % 10)

def main():
    print("\n✨ Let's find the ones digit! ✨\n")  # Start message
    num = int(input("Enter a number: "))  # User input
    print_ones_digit(num)  # Show ones digit
    print("\n✅ Done! Thanks for trying!\n")  # End message

if __name__ == "__main__":
    main()
