# Adds the given data to the list multiple times
def add_custom_copies(my_list, data, num_copies):
    for i in range(num_copies):
        my_list.append(data)  # Add the data to the list

# Main function to run the program
def main():
    # Ask user for the message to copy
    message = input("📥 Enter a message to copy: ")

    # Ask user how many times to add the message
    num_copies = int(input("🔁 How many times do you want to add this message? "))

    # Create an empty list
    my_list = []

    # Show the list before adding anything
    print("\n🗂️ Original list:", my_list)

    # Add the message multiple times using the function
    add_custom_copies(my_list, message, num_copies)

    # Show the updated list and other details
    print("\n🎯 Modified list:", my_list)
    print("➕ Number of copies added:", num_copies)
    print("💬 Message added:", message)

# This ensures the main() runs when the file is executed
if __name__ == "__main__":
    main()
