def get_user_info():
    # User se required information lena
    first_name = input("What is your first name?: ")
    last_name = input("What is your last name?: ")
    email_address = input("What is your email address?: ")
    age = int(input("What is your age?: "))
    city = input("What city do you live in?: ")
    country = input("What country do you live in?: ")
    
    return first_name, last_name, email_address, age, city, country

def main():
    print("\n✨ Welcome to the User Registration ✨\n")  # Starting message
    user_data = get_user_info()  # User info le rahe hain
    
    # Gap for neat output
    print("\n--- Received the following user data ---\n")
    print(user_data)  # User data print karwana

    # Age validation
    if user_data[3] >= 18:
        print("✅ You are eligible to sign up!")
    else:
        print("❌ You are not eligible to sign up!")

    # Gap before the end
    print("\n--- End of Registration ---\n")  # Ending message

if __name__ == "__main__":
    main()
