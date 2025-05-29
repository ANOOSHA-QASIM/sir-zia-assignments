class Student:
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks

    def display(self):
        print("\n" + "-" * 40)
        print("📘 STUDENT INFORMATION 📘".center(40))
        print("-" * 40)
        print(f"👤 Name  : {self.name}")
        print(f"📝 Marks : {self.marks}")
        print("-" * 40 + "\n")


class BankAccount:
    def __init__(self, account_holder, balance):
        self.account_holder = account_holder
        self.balance = balance

    def deposit(self, amount):
        print("\n💰 Deposit Section")
        print("-" * 40)
        if amount > 0:
            self.balance += amount
            print(f"✅ Deposited: {amount}")
            print(f"💼 New Balance: {self.balance}")
        else:
            print("❌ Deposit amount must be positive.")
        print("-" * 40)

    def withdraw(self, amount):
        print("\n🏧 Withdraw Section")
        print("-" * 40)
        if self.balance >= amount:
            self.balance -= amount
            print(f"✅ Withdrew: {amount}")
            print(f"💼 New Balance: {self.balance}")
        else:
            print("❌ Insufficient funds!")
        print("-" * 40)

    def display(self):
        print("\n" + "=" * 40)
        print("🏦 BANK ACCOUNT SUMMARY 🏦".center(40))
        print("=" * 40)
        print(f"👤 Account Holder: {self.account_holder}")
        print(f"💰 Current Balance: {self.balance}")
        print("=" * 40 + "\n")


# Create objects and call methods
student1 = Student("Anusha Qasim", 92)
student1.display()

anusha_account = BankAccount("Anusha Qasim", 5000)
anusha_account.display()
anusha_account.deposit(2000)
anusha_account.withdraw(3000)
anusha_account.withdraw(5000)
