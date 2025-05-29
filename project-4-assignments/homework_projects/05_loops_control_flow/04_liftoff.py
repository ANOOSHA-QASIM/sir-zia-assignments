def main():
    # 🌠 Display heading
    print("\n🌠 Custom Countdown Challenge 🚀")

    # 🔢 Get starting number from user
    start = int(input("🔢 Enter starting number for countdown: "))

    print("\n🕒 Countdown starting...\n")

    # 🔁 Loop from start to 1 (reverse order)
    for i in range(start, 0, -1):
        print(f"{i} ⏳")  # 👉 Print each number on a new line

    # 🚀 Final message
    print("\n🚀 Liftoff! Let's gooo! 🌌")

if __name__ == "__main__":
    main()
    # 👋 Goodbye message
    print("\n🌟 Thanks for launching with us! Bye bye 👋")
