def count_even(lst):
    # Store all even numbers from the list
    even_nums = [num for num in lst if num % 2 == 0]
    
    print("\n✨ Processing your list...")

    if even_nums:
        print(f"\n✅ Even numbers in the list: {', '.join(map(str, even_nums))}")
        print(f"🔢 Total even numbers: {len(even_nums)}")
    else:
        print("\n❌ No even numbers found!")

    print("\n🎉 Task completed. Thanks for using our counter!\n")


def get_list_of_ints():
    # Take numbers from user until Enter is pressed
    lst = []
    user_input = input("🔢 Enter an integer or press Enter to stop: ")
    while user_input != "":
        lst.append(int(user_input))
        user_input = input("🔢 Enter an integer or press Enter to stop: ")
    return lst


def main():
    print("\n🚀 Welcome to the Even Number Counter Challenge!\n")
    lst = get_list_of_ints()
    count_even(lst)


if __name__ == '__main__':
    main()
