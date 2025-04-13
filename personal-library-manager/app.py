# Empty list to store books
library = []

# Function to add a book
def add_book():
    title = input("📚 Enter the book title: ")
    author = input("✍️ Enter the author: ")
    year = int(input("📅 Enter the publication year: "))
    genre = input("📖 Enter the genre: ")
    read_status = input("📚 Have you read this book? (yes/no): ").lower() == "yes"
    
    # Store book details as a dictionary
    book = {
        "title": title,
        "author": author,
        "year": year,
        "genre": genre,
        "read": read_status
    }
    library.append(book)
    print("✅ Book added successfully!")

# Function to remove a book
def remove_book():
    title = input("❌ Enter the title of the book to remove: ")
    for book in library:
        if book["title"].lower() == title.lower():
            library.remove(book)
            print(f"✅ Book '{title}' removed successfully!")
            return
    print(f"❌ Book '{title}' not found.")

# Function to search for a book
def search_book():
    search_by = input("🔍 Search by:\n1. Title\n2. Author\nEnter your choice: ")
    if search_by == "1":
        title = input("📚 Enter the title: ")
        results = [book for book in library if title.lower() in book["title"].lower()]
    elif search_by == "2":
        author = input("✍️ Enter the author: ")
        results = [book for book in library if author.lower() in book["author"].lower()]
    else:
        print("❌ Invalid option.")
        return
    
    if results:
        print("🔍 Matching Books:")
        for book in results:
            read_status = "✔️ Read" if book["read"] else "❌ Unread"
            print(f"{book['title']} by {book['author']} ({book['year']}) - {book['genre']} - {read_status}")
    else:
        print("❌ No matching books found.")

# Function to display all books
def display_books():
    if not library:
        print("📖 No books in the library.")
    else:
        for book in library:
            read_status = "✔️ Read" if book["read"] else "❌ Unread"
            print(f"{book['title']} by {book['author']} ({book['year']}) - {book['genre']} - {read_status}")

# Function to display statistics
def display_statistics():
    total_books = len(library)
    read_books = sum(1 for book in library if book["read"])
    percentage_read = (read_books / total_books) * 100 if total_books > 0 else 0
    print(f"📊 Total books: {total_books}")
    print(f"📊 Percentage read: {percentage_read:.2f}%")

# Menu system
def menu():
    while True:
        print("\n[MENU]")
        print("1. Add a book 📚")
        print("2. Remove a book ❌")
        print("3. Search for a book 🔍")
        print("4. Display all books 📖")
        print("5. Display statistics 📊")
        print("6. Exit 🚪")
        choice = input("Enter your choice: ")

        if choice == "1":
            add_book()
        elif choice == "2":
            remove_book()
        elif choice == "3":
            search_book()
        elif choice == "4":
            display_books()
        elif choice == "5":
            display_statistics()
        elif choice == "6":
            print("Goodbye! 👋")
            break
        else:
            print("❌ Invalid choice. Please try again.")

# Run the program
if __name__ == "__main__":
    menu()
