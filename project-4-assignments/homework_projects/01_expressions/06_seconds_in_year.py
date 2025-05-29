# Constants for time calculations
DAYS_IN_NORMAL_YEAR = 365
DAYS_IN_LEAP_YEAR = 366
HOURS_PER_DAY = 24
MINUTES_PER_HOUR = 60
SECONDS_PER_MINUTE = 60

def main():
    # Calculate seconds in a normal year
    seconds_normal = DAYS_IN_NORMAL_YEAR * HOURS_PER_DAY * MINUTES_PER_HOUR * SECONDS_PER_MINUTE

    # Calculate seconds in a leap year
    seconds_leap = DAYS_IN_LEAP_YEAR * HOURS_PER_DAY * MINUTES_PER_HOUR * SECONDS_PER_MINUTE

    # Print results with emojis
    print("📅 There are " + str(seconds_normal) + " seconds in a normal year! ⏰")
    print("🗓️ There are " + str(seconds_leap) + " seconds in a leap year! 🚀")

# Run the program
if __name__ == '__main__':
    main()
