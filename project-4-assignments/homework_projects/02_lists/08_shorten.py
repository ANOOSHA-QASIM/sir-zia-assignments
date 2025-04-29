MAX_LENGTH: int = 3  # 📏 Maximum list size allowed

def shorten(lst):
    print("\n⚙️ Shortening the list if needed...\n")
    while len(lst) > MAX_LENGTH:
        removed_item = lst.pop()  # 🗑 Remove the last item
        print(f"❌ Removed: {removed_item}")
    print("\n✅ Final list:", lst)

def get_lst():
    """
    📥 Get a list of items from the user.
    """
    my_list = []
    print("👋 Let's create your list. Type something and press Enter.")
    print("⛔ Press Enter without typing anything to finish.\n")
    item = input("🔹 Enter item: ")
    while item != "":
        my_list.append(item)
        item = input("🔹 Enter another item (or press Enter to stop): ")
    return my_list

def main():
    user_list = get_lst()
    shorten(user_list)

# 🚀 Start the program
if __name__ == '__main__':
    main()
