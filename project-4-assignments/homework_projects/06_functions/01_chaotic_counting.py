import random

# 20% chance of stopping
DONE_LIKELIHOOD = 0.2

my_list = []

# Check if chaos stops
def done():
    return random.random() < DONE_LIKELIHOOD

# Count and collect numbers
def chaotic_counting():
    for i in range(20):
        curr_num = i + 1
        if done():
            print("\nOh no! Chaos stopped us early 😱")
            return
        my_list.append(curr_num)
        print(f"Collected: {curr_num}")

def main():
    print("\n✨ Starting the chaotic collection! ✨\n")
    
    chaotic_counting()
    
    # Check if no numbers were collected
    if len(my_list) == 0:
        print("Oops! Chaos didn’t let us collect even one number 😅")
    else:
        print(f"\nCollected Numbers: {my_list}")

    print("\n✅ Mission ended. See you next time! 🔚")

if __name__ == "__main__":
    main()
