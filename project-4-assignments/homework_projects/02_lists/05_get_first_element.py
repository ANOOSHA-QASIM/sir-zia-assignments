def get_first_element(lst):
    """
    Prints the first element of the provided list with a friendly message. 😊
    """
    if len(lst) > 0:
        print(f"\n🎉 The first element in your list is: {lst[0]} 🎉")
    else:
        print("😞 Oh no! The list is empty. Please add some items first. 😞")

def get_lst():
    """
    Prompts the user to enter elements of the list one by one and returns the list. 📝
    """
    lst = []
    elem = input("🖊️ Enter an item to add to your list (leave empty to stop): ")
    
    while elem != "":
        lst.append(elem)  # Add the element to the list
        elem = input("🖊️ Enter another item (or press Enter to finish): ")
    
    return lst

def main():
    print("\nWelcome to the List Program! Let's get started. 🚀\n")
    lst = get_lst()  # Get the list from the user
    get_first_element(lst)  # Show the first element

if __name__ == '__main__':
    main()  # Start the program


