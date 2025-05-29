class Logger:
    def __init__(self):
        print("\n🟢 Logger initialized.")

    def __del__(self):
        print("🔴 Logger deleted.")


log = Logger()
print("--- Program is running ---\n")
del log
print("--- Program finished ---\n")


class FileHandler:
    def __init__(self):
        print("📂 File opened.")

    def __del__(self):
        print("🗂️  File closed.\n")
        

file = FileHandler()
del file
