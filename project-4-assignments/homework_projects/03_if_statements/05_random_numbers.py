import random  # 🎲 Import random module to generate numbers

N_NUMBERS = 10  # 🔢 Number of random values to generate

def main():
    print("🌟 Random Number Generator 🌟\n")

    total_sum = 0  # ➕ Initialize total sum
    print("🎲 Random Numbers:\n")

    for i in range(N_NUMBERS):
        num = random.randint(1, 100)  # 🔁 Generate random number between 1-100
        print(f"{num}", end="  ")  # 🖨️ Print the number with space
        total_sum += num  # ➕ Add to total

    print(f"\n\n🧮 Total Sum: {total_sum}")  # 🧾 Show the final sum

if __name__ == "__main__":
    main()
