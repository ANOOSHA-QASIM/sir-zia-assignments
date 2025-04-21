low = 1
high = 100
attempts = 0
max_attempts = 6

print("\n" + "="*50)
print("🎮 WELCOME TO THE NUMBER GUESSING GAME 🎮")
print("="*50 + "\n")

print("🤔 Think of a number between 1 and 100, and I (computer) will guess it!\n")

while attempts < max_attempts:
    guess = (low + high) // 2
    print(f"🤖 Is your number {guess}?")
    attempts += 1

    feedback = input("Enter 'h' if too high, 'l' if too low, or 'c' if correct: ").lower()
    
    print("-" * 40) 

    if feedback == 'c':
        print("\n" + "="*50)
        print(f"🎉 Yay! I guessed your number {guess} in {attempts} attempts. 🤖")
        print("="*50 + "\n")
        break
    elif feedback == 'l':
        low = guess + 1
    elif feedback == 'h':
        high = guess - 1 
    else:
        print("⚠️ Invalid input! Please enter 'h', 'l', or 'c'.\n")

    if attempts < max_attempts:
        remaining_attempts = max_attempts - attempts
        attempt_word = "attempt" if remaining_attempts == 1 else "attempts"
        print(f"🔄 I have {remaining_attempts} {attempt_word} left.\n")

if attempts == max_attempts and feedback != 'c':
    print("\n" + "="*50)
    print("❌❌❌ GAME OVER ❌❌❌")
    print("I couldn't guess your number... 😞")
    print("🏆 CONGRATULATIONS! YOU WON! 🎉")
    print("="*50 + "\n")
