import random

choices = ["rock" , "paper" , "scissor"]

user_choice = input("Enter rock, papaer or scissor: ").lower()
computer_choice = random.choice(choices)

print(f"\nYour choice {user_choice}")
print(f"Computer choice {computer_choice}")

if user_choice == computer_choice:
    print("It's a tie!")

elif (user_choice == "rock" and computer_choice == "scissor") or\
     (user_choice == "scissor" and computer_choice == "paper") or\
     (user_choice == "paper" and computer_choice == "rock"):
    print("Congratulations You Win!")

else:
    print("Computer Wins")
