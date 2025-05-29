def get_user_numbers():
    # Get numbers from user
    numbers = []

    while True:
        user_input = input("Enter a number (or press Enter to stop): ")

        if user_input == "":
            break

        try:
            num = int(user_input)
            numbers.append(num)
        except ValueError:
            print("⚠️ Invalid input, please enter a valid number!")

    return numbers

def count_nums(num_list):
    # Count how many times each number appears
    count_dict = {}

    for num in num_list:
        if num not in count_dict:
            count_dict[num] = 1
        else:
            count_dict[num] += 1

    return count_dict

def print_num_count(counts):
    # Print only numbers that appear 2 or more times
    print("\n🔁 Repeated Numbers:\n")
    for num in sorted(counts):
        if counts[num] >= 2:
            print(f"🎲 Number {num} appeared {counts[num]} times.\n")

def main():
    print("\n📊 Welcome to Number Counter!")
    print("🧮 I will count how many times each number appears.")
    print("💡 Enter numbers one by one. Press Enter to finish.\n")

    numbers = get_user_numbers()
    counts = count_nums(numbers)
    print_num_count(counts)

if __name__ == "__main__":
    main()
