def get_name():
    return "Sophia"  # Default name, can be modified for specific functionality

def main():
    # Start message
    print("\n🎉 Let's start spreading some good vibes! 🌟\n")

    # User inputs multiple names
    names = []
    while True:
        name = input("Enter a name or press Enter to stop: ")
        if name == "":
            break
        names.append(name)

    # Greet all entered names
    if names:
        print("\n🌈 Time to say hi to everyone! 🎉")
        for name in names:
            print(f"Hey {name}, you're amazing! 🌟 Have a fantastic day ahead! ✨")
    else:
        print("No names entered, but you're still awesome! 😎")

    # End message
    print("\n✅ All greetings sent! Stay happy and shine bright! 🌟\n")

if __name__ == '__main__':
    main()
