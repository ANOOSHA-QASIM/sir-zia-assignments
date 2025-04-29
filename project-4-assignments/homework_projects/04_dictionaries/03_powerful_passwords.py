from hashlib import sha256

def login(email, stored_login, password_to_check):
    # Check if email exists and the hashed password matches
    if email in stored_login and stored_login[email] == hash_password(password_to_check):
        return True
    else:
        return False

def hash_password(password):
    return sha256(password.encode()).hexdigest()

def main():
    print("\n📖 Welcome to the Emoji Password Manager!")
    print("💡 Tip: Use strong passwords for better security.\n")

    # Start with empty login data
    stored_login = {}

    # Register user
    user_email = input("📧 Register - Enter your email: ")
    user_password = input("🔐 Register - Enter your password: ")
    hashed = hash_password(user_password)
    stored_login[user_email] = hashed
    print("🔒 Your password has been hashed as:")
    print(f"➡️  {hashed}")  # 👈 This line shows the hashed password
    print("✅ Registration successful!\n")

    # Login
    login_email = input("📧 Login - Enter your email: ")
    login_password = input("🔑 Login - Enter your password: ")

    if login(login_email, stored_login, login_password):
        print("🎉 Login successful!")
    else:
        print("❌ Invalid email or password!")

if __name__ == "__main__":
    main()
