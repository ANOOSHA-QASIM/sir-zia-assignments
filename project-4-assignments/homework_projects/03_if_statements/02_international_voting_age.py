# Voting ages for fictional countries
PETURKSBOUIPO_AGE = 16
STANLAU_AGE = 25
MAYENGUA_AGE = 48

def main():
    # Taking user input
    name = input("📝 Please enter your name: ")
    age = int(input("🎂 Please enter your age: "))

    # Welcome message
    print(f"\n👋 Hello, {name.upper()}! Welcome to the Voting Age Checker!\n")
    print("🔎 Checking your voting eligibility in 3 fictional countries...\n")

    # Peturksbouipo check
    if age >= PETURKSBOUIPO_AGE:
        print(f"✅ You can vote in Peturksbouipo (Voting age: {PETURKSBOUIPO_AGE})\n")
    else:
        print(f"❌ You cannot vote in Peturksbouipo (Voting age: {PETURKSBOUIPO_AGE})\n")

    # Stanlau check
    if age >= STANLAU_AGE:
        print(f"✅ You can vote in Stanlau (Voting age: {STANLAU_AGE})\n")
    else:
        print(f"❌ You cannot vote in Stanlau (Voting age: {STANLAU_AGE})\n")

    # Mayengua check
    if age >= MAYENGUA_AGE:
        print(f"✅ You can vote in Mayengua (Voting age: {MAYENGUA_AGE})\n")
    else:
        print(f"❌ You cannot vote in Mayengua (Voting age: {MAYENGUA_AGE})\n")

    # End message
    print("🎉 Done! Thanks for checking your voting eligibility.\n")

# Program execution starts here
if __name__ == '__main__':
    main()
