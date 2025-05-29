class TemperatureConverter:
    @staticmethod
    def celsius_to_fahrenheit(c):
        return (c * 9/5) + 32


# Example usage
celsius_temp = 37
fahrenheit = TemperatureConverter.celsius_to_fahrenheit(celsius_temp)

# Output
print("\n" + "=" * 40)
print(f"🌡️ Celsius     : {celsius_temp}°C")
print(f"🔥 Fahrenheit  : {fahrenheit}°F")
print("=" * 40 + "\n")  
