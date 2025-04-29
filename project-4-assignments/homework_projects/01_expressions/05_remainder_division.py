def main():
    # Get numbers from the user
    dividend: int = int(input("Please enter an integer to be divided: "))  # First number
    divisor: int = int(input("Please enter an integer to divide by: "))    # Second number

    # Check if divisor is zero
    if divisor == 0:
        print("Error: Cannot divide by zero! Please try again with a valid number.")
    else:
        # Calculate quotient and remainder
        quotient: int = dividend // divisor
        remainder: int = dividend % divisor

        # Print the result
        print(f"The result of this division is {quotient} with a remainder of {remainder}")


# Run the program
if __name__ == '__main__':
    main()
