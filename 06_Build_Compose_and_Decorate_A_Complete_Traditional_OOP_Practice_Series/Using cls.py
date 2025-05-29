class Counter:
    count = 0 

    def __init__(self):
        Counter.count += 1 

    @classmethod
    def show_count(cls):
        print("\n" + "=" * 40)
        print("📊 OBJECT CREATION TRACKER".center(40))
        print("=" * 40)
        print(f"🧮 Total Objects Created: {cls.count}")
        print("=" * 40 + "\n")

obj1 = Counter()
obj2 = Counter()
obj3 = Counter()

Counter.show_count()

class Employee:
    emp_count = 0 

    def __init__(self, name, position):
        Employee.emp_count += 1  
        self.id = Employee.emp_count 
        self.name = name
        self.position = position

    def display_info(self):
        print("\n" + "-" * 40)
        print("👔 EMPLOYEE INFORMATION".center(40))
        print("-" * 40)
        print(f"🆔 ID        : {self.id}")
        print(f"👤 Name      : {self.name}")
        print(f"💼 Position  : {self.position}")
        print("-" * 40)

    @classmethod
    def show_emp_count(cls):
        print("\n" + "=" * 40)
        print("📊 TOTAL EMPLOYEES".center(40))
        print("=" * 40)
        print(f"📌 Total Employees Created: {cls.emp_count}")
        print("=" * 40)


#create objects and call methods
emp1 = Employee("Anusha Qasim", "Frontend Developer")
emp2 = Employee("John Doe", "Data Scientist")
emp3 = Employee("Ayesha Khan", "UI/UX Designer")


emp1.display_info()
emp2.display_info()
emp3.display_info()

Employee.show_emp_count()



