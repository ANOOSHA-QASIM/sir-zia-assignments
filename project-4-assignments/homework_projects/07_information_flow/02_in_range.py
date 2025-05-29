def in_range(n, low, high) -> bool:
    """Check if a number is within the given range."""
    if low > high:
        return None  # Invalid range
    return low <= n <= high  # Check if in range


def main():
    print("\n✨ Range Checker Program ✨\n")

    # Get user input
    n = int(input("🔢 Enter a number: "))
    low = int(input("🔽 Enter the lower bound: "))
    high = int(input("🔼 Enter the upper bound: "))

    print("\n--- Result ---\n")

    result = in_range(n, low, high)

    # Display results
    if result is None:
        print(f"⚠️ Invalid range! Lower bound {low} must be less than upper bound {high}.")
    elif result:
        print(f"✅ {n} is in the range [{low}, {high}].")
    else:
        print(f"❌ {n} is not in the range [{low}, {high}].")

    print("\n--- End of Program ---\n")


if __name__ == "__main__":
    main()
