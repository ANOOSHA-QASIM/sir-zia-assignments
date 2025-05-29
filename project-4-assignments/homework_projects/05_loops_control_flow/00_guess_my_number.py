import random

def main():
    # Generate a random number between 1 and 100
    secret_number = random.randint(1, 100)

    # 🟢 Welcome message
    print("\n🎮 Welcome to 'Guess My Number' Game! 🎉")
    print("🤖 I have picked a number between 1 and 100.")
    print("🔍 Try to guess it!\n")

    attempts = 0  # Track number of guesses

    # 🔢 First guess
    guess = int(input("👉 Take a guess: "))
    attempts += 1

    # 🔁 Keep asking until the guess is correct
    while guess != secret_number:
        if guess < secret_number:
            print("⬇️  Too low!\n")
        else:
            print("⬆️  Too high!\n")
        
        # 🔄 New guess
        guess = int(input("👉 Try again: "))
        attempts += 1

    # 🏁 Success message
    print(f"\n✅ Congratulations! You guessed the correct number {secret_number} 🎯")
    print(f"🧠 Total attempts: {attempts}")
    print("🌟 Well done! You're a number guessing champ! 🏆\n")

# 🚀 Start the game
if __name__ == "__main__":
    main()
