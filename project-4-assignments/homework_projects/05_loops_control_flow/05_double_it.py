def main():
    # 🌟 Welcome message
    print("\n🚀 Welcome to the Doubling Challenge! Let's get started! 🌟\n")

    # 🔢 User input
    curr_value = int(input("🔢 Enter a number to start doubling: "))

    # Lists to store even and odd numbers
    even_numbers, odd_numbers = [], []

    # Loop to calculate even and odd numbers
    for i in range(10):
        even_number = curr_value * 2  # Even number
        odd_number = curr_value * 2 + 1  # Odd number

        even_numbers.append(even_number)
        odd_numbers.append(odd_number)

        curr_value = even_number  # Update for next iteration

    # Display results
    print("\n🌟 Even Numbers:", *even_numbers)
    print("\n🌟 Odd Numbers:", *odd_numbers)

if __name__ == "__main__":
    main()
    # 👋 Goodbye message
    print("\n🌟 Thanks for doubling with us! Bye bye 👋\n")
