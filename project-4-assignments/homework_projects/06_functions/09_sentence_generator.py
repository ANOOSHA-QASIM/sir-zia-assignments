def make_sentence(word, part_of_speech):
    # Sentence based on word type
    if part_of_speech == 0:
        print(f"\n📦 I am excited to add this {word} to my vast collection of them!")
    elif part_of_speech == 1:
        print(f"\n🏃 It's so nice outside today it makes me want to {word}!")
    elif part_of_speech == 2:
        print(f"\n🌤️ Looking out my window, the sky is big and {word}!")
    else:
        print("\n❌ Invalid choice! Please enter 0, 1, or 2.")

def main():
    print("\n🌟 Welcome to the Sentence Maker! 🌟")

    word = input("\n✍️  Please type a noun, verb, or adjective: ")
    print("\n🔢 What type of word is it?")
    print("Type 0 for noun 🧸, 1 for verb 🕺, 2 for adjective 🎨")

    try:
        part_of_speech = int(input("\n👉 Your choice: "))
        make_sentence(word, part_of_speech)
    except ValueError:
        print("\n🚫 Please enter a valid number (0, 1, or 2).")

    print("\n✅ Thanks for playing with words! Come again! 😊\n")

if __name__ == '__main__':
    main()
