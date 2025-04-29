def main():
    print("🌟 Leap Year Checker 🌟\n")

    start_yaer = int(input("📅 Please enter the start year: "))
    end_year = int(input("📅 Please enter the end year: "))

    total_leap_years = 0

    for year in range(start_yaer, end_year + 1):
        if (year % 4 == 0):
            if (year % 100 == 0):
                if (year % 400 == 0):
                    print(f"\n✅ {year} is a leap year.")
                    total_leap_years += 1
                else:
                    print(f"❌ {year} is not a leap year.")
            else:
                # Year is divisible by 4 but not by 100
                # Hence, it is a leap year

                print(f"✅ {year} is a leap year.")
                total_leap_years += 1
        else:
            # Year is not divisible by 4
            # Hence, it is not a leap year

            print(f"❌ {year} is not a leap year.")
    print(f"\n🌈 Total leap years between {start_yaer} and {end_year}: {total_leap_years} 🎉")
    
    print("🎉 Done! Thanks for using the Leap Year Checker. 🚀\n")

if __name__ == "__main__":
    main()
            