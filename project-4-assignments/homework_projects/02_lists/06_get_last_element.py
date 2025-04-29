def get_last_element(lst):
    """
    This function prints the last element of the list.
    """
    print("🎯 The last element in your list is:", lst[-1])

def get_list_from_user():
    """
    This function asks the user to enter list items one by one,
    and returns the complete list.
    """
    lst = []
    print("🛒 Let's make a list! (Press Enter to stop)")
    item = input("👉 Enter an item: ")
    while item != "":
        lst.append(item)
        item = input("👉 Enter another item (or press Enter to stop): ")
    return lst

def show_list(lst):
    """
    This function shows the full list entered by the user.
    """
    print("📦 Here's your full list:", lst)

def main():
    print("👋 Hello! We will find the LAST item in your list 🧐")
    lst = get_list_from_user()
    show_list(lst)
    get_last_element(lst)
    print("✅ All done! Good job! 🚀")

if __name__ == '__main__':
    main()
