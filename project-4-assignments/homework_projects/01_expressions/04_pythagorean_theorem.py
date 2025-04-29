import math  # Import math module to use sqrt() for square root calculation

def main():
    # Get lengths of the two perpendicular sides (AB and AC) from the user
    ab: float = float(input("Enter the length of AB: "))  # Length of side AB
    ac: float = float(input("Enter the length of AC: "))  # Length of side AC

    # Use Pythagorean theorem to calculate the hypotenuse (BC)
    bc: float = math.sqrt(ab**2 + ac**2)  # Calculate the hypotenuse (BC)

    # Round the result to 2 decimal places

    bc_rounded = round(bc, 2)

    # Output the result
    print("The length of BC (the hypotenuse) is: " + str(bc_rounded))  # Print hypotenuse

# Main function execution
if __name__ == '__main__':
    main()  # Call the main function
