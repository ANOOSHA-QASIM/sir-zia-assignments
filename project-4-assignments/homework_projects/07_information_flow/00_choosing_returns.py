IS_ADULT = 18
IS_SENIOR = 60

# Check adult age (18 to 59)
def is_adult(age: int) -> bool:
    return age >= IS_ADULT and age < IS_SENIOR

# Check senior age (60+)
def is_senior(age: int) -> bool:
    return age >= IS_SENIOR

def main():
    print("\n✨ Age Checker Program ✨\n")
    age = int(input("🎂 Enter your age: "))

    print("\n--- Result ---\n")

    if is_adult(age):
        print("✅ You are an adult.\n")
    else:
        print("❌ You are not an adult.\n")

    if is_senior(age):
        print("👴 You are a senior.\n")
    else:
        print("🧒 You are not a senior.\n")

if __name__ == "__main__":
    main()
