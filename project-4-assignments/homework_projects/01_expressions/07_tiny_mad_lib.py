# Sentence ka starting part (template) - Creative Story!
SENTENCE_START: str = "Once upon a time in the magical land of Panaversity, I was learning Python, and suddenly, my "  # Starting template

def main():
    # Adjective input (describing something in an interesting way)
    adjective: str = input("Please type an adjective (e.g. magical, hilarious) and press enter ✨: ")
    
    # Noun input (something funny, cool, or unexpected)
    noun: str = input("Please type a noun (e.g. dragon, unicorn, pizza) and press enter 🦄🍕: ")
    
    # Verb input (something funny or unexpected action)
    verb: str = input("Please type a verb (e.g. fly, dance, teleport) and press enter 🕺💫: ")

    # Using f-strings to format the story
    print("\nHere's your fun and magical story! ✨")
    print(f"{SENTENCE_START}{adjective} {noun} suddenly appeared! It started to {verb} like a pro! 🏆👑")
    print(f"Everyone in Panaversity was amazed and cheered: 'Wow! That is some crazy {adjective} {noun} magic!' 🔮")

if __name__ == '__main__':
    main()
