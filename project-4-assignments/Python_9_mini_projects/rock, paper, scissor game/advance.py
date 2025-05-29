import random

choices = ["rock" , "paper" , "scissor"]

user_score = 0
computer_score = 0
rounds = 3

print("🔥 Welcome to Rock-Paper-Scissors! Best of 3 Rounds 🔥\n") 

for i in range(rounds):
    print(f"Rounds {i+1}")

    user_choice = input("Enter rock, papaer or scissor: ").lower()
    computer_choice = random.choice(choices)

    print(f"Computer choice {computer_choice}")

    if user_choice == computer_choice:
        print("It's a tie!\n")

    elif (user_choice == "rock" and computer_choice == "scissor") or\
         (user_choice == "scissor" and computer_choice == "paper") or\
         (user_choice == "paper" and computer_choice == "rock"):
         print("You win this round! 🎉\n")  
         user_score += 1 
    
    else:
         print("Computer wins this round!\n")  
         computer_score += 1  

print("Final Score")  
print(f"You: {user_score} | Computer: {computer_score}\n")


if user_score > computer_score:  
    print("Congratulations! You won the game!")  
elif user_score < computer_score:  
    print("Computer wins the game! Better luck next time!")  
else:  
    print("It's a draw!") 

   

