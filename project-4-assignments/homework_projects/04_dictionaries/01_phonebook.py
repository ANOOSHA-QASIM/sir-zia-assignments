def read_phone_numbers():
    phonebook = {}  # 📇 Empty phonebook

    while True:
        name = input("📝 Enter name (or press Enter to stop): ")
        if name == "":
            break

        # ⚠️ Check if name already exists
        if name in phonebook:
            choice = input(f"🔁 {name} already exists. Update number? (yes/no): ").lower()
            if choice != "yes":
                print("⏭️ Skipped updating.")
                continue

        number = input(f"📞 Enter phone number for {name}: ")
        phonebook[name] = number  # ➕ Add/Update contact

    return phonebook


def print_phonebook(phonebook):
    print("\n📒 Your Phonebook:\n")
    for name in phonebook:
        print(f"➡️  {name} → {phonebook[name]}")


def look_up_number(phonebook):
    while True:
        name = input("\n🔍 Lookup name (or press Enter to stop): ")
        if name == "":
            break

        if name in phonebook:
            print(f"✅ {name}'s number: {phonebook[name]}")
        else:
            print(f"❌ {name} not found!")


def main():
    print("\n📖 Welcome to the Emoji Phonebook!")
    print("💡 Tip: You can update numbers if names repeat.\n")

    phonebook = read_phone_numbers()
    print_phonebook(phonebook)
    look_up_number(phonebook)


if __name__ == "__main__":
    main()
