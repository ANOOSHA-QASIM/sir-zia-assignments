def print_multiple(message: str, repeats: int):
    for _ in range(repeats):  
        print(message)

def main():
    print("\n✨ Welcome to the Message Repeater! ✨\n")  # Start message
    # Get user input

    message = input("💬 Please type a message: ")  
    repeats = int(input("🔁 Enter a number of times to repeat your message: "))  

    print("\n🎉 Let's start printing your message! 🎉")
    print() 
    
    # Call print_multiple function
    print_multiple(message, repeats)
    print()
    
    print("🎊 Finished printing your message! 🎊\n")

if __name__ == '__main__':
    main()
