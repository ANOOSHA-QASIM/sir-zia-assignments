MINIMUM_HEIGHT = 50  # Minimum height required 🎢

def main():
    while True:
        height = input("\nEnter your height in inches: 👇 ")

        # Empty input ko handle karna
        if height == "":
            print("\nNo input given. Exiting program. 🚪\n")
            break

        try:
            height = float(height)  # Height ko number mein convert karna
        except ValueError:
            print("\nInvalid input. Please enter a valid number for height. ❌\n")
            continue

        # Negative height check
        if height < 0:
            print("\nHeight cannot be negative. Please enter a valid height. ⛔\n")
            continue
        # Too high height check
        if height >= 100:
            print("\nHeight seems too high. Please enter a valid height. 🤨\n")
            continue
        # Zero height check
        if height == 0:
            print("\nHeight cannot be zero. Please enter a valid height. ❌\n")
            continue

        # Checking if height is enough for the ride 🎢
        if height >= MINIMUM_HEIGHT:
            print(f"\nYou are tall enough to ride the roller coaster! 🎢🎉\n")
            break
        else:
            print(f"\nSorry, you are not tall enough to ride the roller coaster. 😢\n")
            continue

if __name__ == "__main__":
    main()
