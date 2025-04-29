import random

NUM_SIDES = 6

def main():
    print("🎲 Welcome to Dice Roller Game 🎲")
    input("Press Enter to roll the dice...")  # User se input lena just to feel interaction

    die1 = random.randint(1, NUM_SIDES)
    die2 = random.randint(1, NUM_SIDES)
    total = die1 + die2

    print("\nRolling the dice...")
    print("🎯 First die:", die1)
    print("🎯 Second die:", die2)
    print("🔢 Total of both dice:", total)

    print("\nGame over. Thanks for playing! 😊")

if __name__ == '__main__':
    main()

