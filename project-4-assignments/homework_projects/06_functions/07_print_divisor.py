def print_divisors(num: int):
    print(f"\n🔍 Divisors of {num} are:", end=' ')
    for i in range(1, num + 1):
        if num % i == 0:
            print(i, end=' ')  # space-separated

def main():
    print("\n✨ Welcome to the Divisor Finder! ✨\n")
    num = int(input("👉 Enter a number: "))
    print_divisors(num)
    print("\n\n✅ Done! Thanks for using the tool! 😊\n")

if __name__ == '__main__':
    main()
