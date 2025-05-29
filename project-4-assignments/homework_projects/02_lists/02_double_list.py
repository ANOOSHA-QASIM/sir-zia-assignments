def main():
    numbers : list[int] = [1 , 2, 3 ,4, 5]
    doubled_numbers : list[int] = []

    for num in numbers:
        doubled_numbers.append(num * 2)

    print(f"🎯 Original list: {numbers}")
    print(f"💥 Doubled list: {doubled_numbers}")


if __name__ == '__main__':
    main()
