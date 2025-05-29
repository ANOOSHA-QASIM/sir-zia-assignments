import random

words_list = ["apple", "pakistan","banana","igloo"]
secret_word = random.choice(words_list)
hidden_word = ["_"] * len(secret_word)
max_attempts = 6
guessed_letters =[]

while max_attempts > 0 and "_" in hidden_word:
    print("\nGuess this word " + " ".join(hidden_word))
    print(f"Guess left: {max_attempts}")
    print(f"Guessed letters {', '.join(guessed_letters)}")

    guess = input("Enter a letter: ").lower()

    if guess in guessed_letters:
        print("You already guessed this letter. Try another one!")
        continue

    guessed_letters.append(guess)

    if guess in secret_word:
        print("Good job! The letter is in the word.")
        for index, letter in enumerate(secret_word):
            if letter == guess:
                hidden_word[index] = guess
               
    else:
        print("Wrong guess! Try again.")
        max_attempts -= 1

if "_" not in hidden_word:
    print(f"\n🎉 Congratulations! You guessed the word: {secret_word} in {max_attempts} attempts")

else:
    print(f"\n😞 You lost! The correct word was: {secret_word}")