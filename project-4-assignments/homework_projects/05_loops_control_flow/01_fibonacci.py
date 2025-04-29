# 🔢 Max limit for Fibonacci sequence
MAX_TERM_VALUE: int = 10000

def main():
    # 🎬 Starting values
    curr_term = 0  # Fib(0)
    next_term = 1  # Fib(1)
    
    fibonacci_numbers = []  # 📦 List to store all terms

    # 💫 Welcome message
    print("\n✨ Welcome to the Fibonacci Checker! ✨")
    print("🔢 Generating numbers up to 10,000...\n")

    # 🔁 Loop to generate sequence
    while curr_term <= MAX_TERM_VALUE:
        print(curr_term, end=" ")        # 🖨️ Print current term
        fibonacci_numbers.append(curr_term)  # 💾 Save in list

        # ➕ Next number
        term_after_next = curr_term + next_term
        curr_term = next_term
        next_term = term_after_next

    print("\n\n🔍 Time to check your number!\n")

    # 🧑‍💻 User input
    user_input = int(input("✏️ Enter a number: "))

    # ✅ Check if it's in the list
    if user_input in fibonacci_numbers:
        print(f"\n🎉 Yes! {user_input} is a Fibonacci number! ✅")
    else:
        print(f"\n🚫 No! {user_input} is not a Fibonacci number. ❌")

    # 🎉 Goodbye message
    print("\n🌟 Thanks for checking Fibonacci numbers with me! See you again! 👋\n")

# 🚀 Run the program
if __name__ == '__main__':
    main()
