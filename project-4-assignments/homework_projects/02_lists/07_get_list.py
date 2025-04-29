def main():
    # 📝 Empty list to store user inputs
    my_list = []

    print("👋 Welcome! Let's create a list together.")
    print("👉 Type something and press Enter to add to the list.")
    print("⛔ Press Enter without typing anything to stop.\n")

    # 📥 First input from user
    value = input("🔹 Enter a value: ")

    # 🔁 Loop until user presses Enter without any input
    while value != "":
        my_list.append(value)  # ➕ Add to list
        value = input("🔹 Enter another value (or press Enter to stop): ")

    # ✅ After the user finishes adding items
    if not my_list:
        print("😕 You didn't add anything to the list!")  # If list is empty
    else:
        print(f"\nYou added {len(my_list)} items to your list.")

    print("📝 Your list:")
    for item in my_list:
        print(f"🔸 {item}")

    # ✅ Done! Show the list
    print("🎉 Good job! You made a list!")

# 🚀 Start the program
if __name__ == '__main__':
    main()
