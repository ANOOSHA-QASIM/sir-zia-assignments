# Affirmation to be typed by the user
AFFIRMATION = "You are capable of achieving great things."

def main():
    # Positive Machine Greeting 🌈
    print("\n🌈 Wholesome Machine 🌈")
    print("🤖 I am here to spread positivity and good vibes!\n")

    # Display the affirmation to the user
    print(f"Please type the following affirmation:")
    print(f"\"{AFFIRMATION}\"\n")

    # Get user input
    user_input = input("✏️ Type the affirmation: ")

    # Loop until correct affirmation is typed
    while user_input != AFFIRMATION:
        print("\n🚫 Oops! That's not quite right.")
        print("Try again! 🤔")
        user_input = input("✏️ Type the affirmation: ")

    # Success message after correct input
    print("\n🎉 Awesome! You got it right! ✅")

# Run the program
if __name__ == "__main__":
    main()
    # Final message 🌟
    print("\n🌟 You are amazing! Keep spreading positivity! 🌟")
    print("👋 Goodbye! Until next time!")
