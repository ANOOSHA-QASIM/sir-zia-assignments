class Employee:
    def __init__(self, name, salary, ssn):
        self.name = name          # Public
        self._salary = salary     # Protected
        self.__ssn = ssn          # Private

    def show_details(self):
        print(f"Name   : {self.name}")
        print(f"Salary : {self._salary}")
        print(f"SSN    : {self.__ssn}")

emp = Employee("Anusha", 50000, "123-45-6789")

print("=" * 40)
print("        EMPLOYEE INFORMATION")
print("=" * 40, "\n")

print("Name       :", emp.name)           # Public access
print("Salary     :", emp._salary)        # Protected access
print("SSN        :", emp._Employee__ssn)  # Private 

print("\n" + "-" * 40)
print("USING METHOD TO PRINT DETAILS".center(40))
print("-" * 40)
emp.show_details()
print()



