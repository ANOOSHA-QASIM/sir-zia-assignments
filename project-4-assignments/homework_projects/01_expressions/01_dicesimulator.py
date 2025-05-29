import random  # To generate random numbers for dice rolls

NUM_SIDES = 6  # A die has 6 sides (1 to 6)

# Rolls two dice and prints the total
def roll_dice():
    die1 = random.randint(1, NUM_SIDES)  # First die roll
    die2 = random.randint(1, NUM_SIDES)  # Second die roll
    total = die1 + die2  # Add both dice
    print("Total of two dice:", total)  # Print total

# Main function starts here
def main():
    die1 = 10  # Local variable (not related to roll_dice)
    print("die1 in main() starts as:", die1)  # Show value before rolling

    roll_dice()  # First roll
    roll_dice()  # Second roll
    roll_dice()  # Third roll

    print("die1 in main() is still:", die1)  # Value remains same (scope example)

# Run the main function when program starts
if __name__ == '__main__':
    main()
