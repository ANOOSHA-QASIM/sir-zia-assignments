def main():
    # User se Fahrenheit mein temperature lena
    fahrenheit = float(input("Enter temperature in Fahrenheit: "))
    
    # Fahrenheit se Celsius mein conversion
    celsius = (fahrenheit - 32) * 5.0 / 9.0

     # Rounding the Celsius value to 2 decimal places
    celsius = round(celsius, 2)
    
    # Result ko print karna
    print(f"Temperature: {fahrenheit}F = {celsius}C")

if __name__ == '__main__':
    main()
