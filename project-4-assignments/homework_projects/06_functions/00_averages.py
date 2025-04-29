# Function to calculate average and round it off 😊
def average(a: float, b: float, c: float):
    total = a + b + c  # ➕
    avg = total / 3     # ➗
    return round(avg, 2)  # 🔢

def main():
    a = float(input("Enter first number: 🔢 "))
    b = float(input("Enter second number: 🔢 "))
    c = float(input("Enter third number: 🔢 "))
    
    avg = average(a, b, c)  # 📊
    print(f"\nThe average of {a}, {b}, and {c} is: {avg} 💡")

if __name__ == "__main__":
    main()
