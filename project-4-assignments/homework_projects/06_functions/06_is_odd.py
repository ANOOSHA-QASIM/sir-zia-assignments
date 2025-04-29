def main():
    start = int(input("\nEnter starting number: "))  # User input for start
    end = int(input("Enter ending number: "))  # User input for end
    
    print("\n🎉 Checking Odd/Even... 🎉\n")
    
    for i in range(start, end + 1):
        if is_odd(i):
            print(f'{i} is odd 🤔\n')
        else:
            print(f'{i} is even ✅\n')

    print("\n🎊 Done! 🎊\n")

def is_odd(value: int):
    return value % 2 != 0  # Return True if odd

if __name__ == '__main__':
    main()  # Start program
