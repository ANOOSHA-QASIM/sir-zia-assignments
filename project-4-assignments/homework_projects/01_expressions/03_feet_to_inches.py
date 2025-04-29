INCHES_IN_FOOT = 12  # 1 foot = 12 inches (conversion constant)

def main():
    feet = float(input("Enter number of feet: "))  # Take input in feet from user
    inches = feet * INCHES_IN_FOOT  # Convert feet to inches
    print("That is", inches, "inches!")  # Show result to user

if __name__ == '__main__':
    main()
