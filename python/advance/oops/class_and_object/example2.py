class Student:
    def __init__(self, roll_no, name, standard):
        self.roll_no = roll_no
        self.name = name
        self.standard = standard

    def display_info(self):
        print(f"Roll No. : {self.roll_no}")
        print(f"Name : {self.name}")
        print(f"Standard : {self.standard}")

student1 = Student(1, "John", 12)
student1.display_info()

student2 = Student(2, "Zayn", 12)
student2.display_info()