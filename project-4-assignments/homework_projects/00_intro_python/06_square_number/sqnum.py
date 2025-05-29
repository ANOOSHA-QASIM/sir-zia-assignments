def main():
    num: float = float(input("Type a number to see its square: "))  # Ask the user for a number and convert it to float
    print(str(num) + " squared is " + str(num ** 2))  # Display the square of the number

if __name__ == '__main__':
    main()
