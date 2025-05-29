# Employee class
class Employee:
    def __init__(self, name):
        self.name = name

    def show(self):
        print(f"👩 Employee Name: {self.name}")

# Department class
class Department:
    def __init__(self, dept_name, employee):  # Aggregation
        self.dept_name = dept_name
        self.employee = employee

    def show_details(self):
        print(f"\n🏢 Department : {self.dept_name}")
        self.employee.show()

# Objects
emp1 = Employee("Anusha Qasim")
dept = Department("Software Development", emp1)

# Output
print("\n" + "=" * 40)
print("       📋 DEPARTMENT DETAILS")
print("=" * 40)
dept.show_details()
print("\n" + "=" * 40)