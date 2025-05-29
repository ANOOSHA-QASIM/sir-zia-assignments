# Decorator function
def log_function_call(func):
    def wrapper():
        print("\nFunction is being called")
        func()
    return wrapper

# Use decorator
@log_function_call
def say_hello():
    print("Hello!\n")

say_hello()
