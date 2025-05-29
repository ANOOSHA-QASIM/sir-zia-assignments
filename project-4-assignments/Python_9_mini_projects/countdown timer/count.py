import time

total_time = int(input("Enter time in seconds for countdown: "))

def countdown(total_time):
    while total_time >= 0:
        mins, secs = divmod(total_time, 60)
        print(f"\r{mins:02}:{secs:02}", end="" ,flush=True)

        time.sleep(1)
        total_time -= 1

    print("\r00:00")
    print("Times Up!")

countdown(total_time)