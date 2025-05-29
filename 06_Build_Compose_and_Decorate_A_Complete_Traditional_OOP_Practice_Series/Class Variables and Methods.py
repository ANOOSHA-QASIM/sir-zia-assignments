class Bank:
    bank_name = "National Bank of Pakistan"

    @classmethod
    def change_bank_name(cls, new_name):
        cls.bank_name = new_name

bank1 = Bank()
bank2 = Bank()

print("=" * 40)
print("BANK INFORMATION".center(40))
print("=" * 40)
print(bank1.bank_name)
print(bank2.bank_name)

Bank.change_bank_name("State Bank of Pakistan")

print("\nAfter changing bank name:")
print("=" * 40)
print(bank1.bank_name)
print(bank2.bank_name)


class Library:
    library_name = "City Public Library"

    def __init__(self, book_count):
        self.book_count = book_count

    @classmethod
    def change_library_name(cls, new_name):
        cls.library_name = new_name

    def display_info(self):
        print("Library Name:", Library.library_name)
        print("Total Books:", self.book_count)


lib1 = Library(1000)
lib2 = Library(2000)

print("\n" + "=" * 40)
print("LIBRARY INFORMATION".center(40))
print("=" * 40)

print("Before changing library name:")
lib1.display_info()
print("-" * 40)
lib2.display_info()

Library.change_library_name("Downtown Public Library")

print("\nAfter changing library name:")
lib1.display_info()
print("-" * 40)
lib2.display_info()
