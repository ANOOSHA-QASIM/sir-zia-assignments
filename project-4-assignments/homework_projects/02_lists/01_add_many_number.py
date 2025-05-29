# 📌 Adds all numbers in the list and returns the total
def add_numbers(numbers: list[int]) -> int:
    total = 0
    for num in numbers:
        total += num
    return total

# 🚀 Runs the program
def main():
    my_list: list[int] = [5, 15, 25, 35]  # List of numbers
    result: int = add_numbers(my_list)  # Calculate sum
    print(f"🧮 Total sum is: {result}")  # Show the result

# ▶️ Start the program
if __name__ == '__main__':
    main()
