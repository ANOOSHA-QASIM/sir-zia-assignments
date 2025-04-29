def main():
    print()

    name = input("👤 Enter your name: ")

    print()

    language = input("🌐 What's your preferred language (English/Spanish/French/Urdu)? ")

    print("\n")

    print(greet(name, language))

    print()


def greet(name, language) -> str:
    if language.lower() == "english":
        return f"👋 Hello, {name}! Welcome to the program."

    elif language.lower() == "spanish":
        return f"🎉 ¡Hola, {name}! Bienvenido al programa."

    elif language.lower() == "french":
        return f"🥖 Bonjour, {name}! Bienvenue dans le programme."

    elif language.lower() == "urdu":
        return f"🌙 Salam, {name}! Program mein khush amdeed."

    else:
        return f"❗ Sorry, I don’t know that language."


if __name__ == "__main__":
    main()
