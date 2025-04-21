import random

secret_num = random.randint(1, 100)
attempts = 0 
max_attempts = 6

print("Welcome to the 'Guess the number' Game")
print("I have selected a number between 1 and 100")
print(f"You have {max_attempts} attempts to guess it correctly. Let's start!")

while attempts < max_attempts:

    guess = int(input("\nEnter your guess: "))
    attempts += 1

    if guess < secret_num :
        print(f"\nToo low! Try a higher number. ({max_attempts - attempts} attempts left)")
    
    elif guess > secret_num :
        print(f"\nToo high! Try a lower number. ({max_attempts - attempts} attempts left)")
    
    else:
        print(f"\nCongratulations! You guess the correct number in {attempts} attempts. ")
        break

if attempts == max_attempts and guess != secret_num:
    print(f" \nGame Over! The correct number was {secret_num}. Better luck next time!")