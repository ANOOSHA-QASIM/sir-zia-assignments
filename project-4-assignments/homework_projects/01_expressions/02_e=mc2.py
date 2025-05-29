C = 299792458  # Speed of light in meters per second (constant)

def main():
    mass_in_kg = float(input("\nEnter mass in kg: "))  # Get mass from user

    energy_in_joules = mass_in_kg * (C ** 2)  # E = m * c^2

    # Print results
    print("e = m * C^2...")
    print("m = " + str(mass_in_kg) + " kg")
    print("C = " + str(C) + " m/s  ")
    print(str(energy_in_joules) + " joules of energy! \n")

if __name__ == '__main__':
    main()
