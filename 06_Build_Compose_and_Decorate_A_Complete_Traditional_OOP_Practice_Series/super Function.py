class Student:
    def __init__(self, name):
        self.name = name

class Teacher(Student):
    def __init__(self, name, subject):
        super().__init__(name)
        self.subject = subject

    def display(self):
        print("\n" + "=" * 40)
        print("         TEACHER INFORMATION")
        print("=" * 40)
        print("Name    :", self.name)
        print("Subject :", self.subject + "\n")

# Create and display
teacher1 = Teacher("Anusha Qasim", "Mathematics")
teacher1.display()


