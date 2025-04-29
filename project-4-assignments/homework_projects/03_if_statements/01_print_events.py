def main():
    print("🌟 First 20 Even Numbers using range(start, end, step) 🌟\n")
    
    # Adding emojis to the message before the numbers
    print("🔢 Even Numbers: ✨", end=" ")

    for num in range(0, 40, 2):
        print(num, end=" ")  # Print all numbers in one line

    print("\n\n🎉 All even numbers printed successfully! 🚀")  # Final success message

if __name__ == "__main__":
    main()
