class Book:
    total_books = 0  # Class variable

    def __init__(self, title):
        self.title = title
        Book.increment_book_count()

    @classmethod
    def increment_book_count(cls):
        cls.total_books += 1

    def show_info(self):
        print(f"📚 Book Title: {self.title}")

# Create Book Objects
book1 = Book("Python Basics")
book2 = Book("Learn JavaScript")

# Show info
print("\n" + "=" * 40)
print("           BOOK INFORMATION")
print("=" * 40)
book1.show_info()
book2.show_info()

# Show total books
print(f"\n📖 Total Books Added: {Book.total_books}\n")
