class Student:
    def set_details(self , name , marks):
        self.name = name
        self.marks = marks

    def show_details(self):
        print(f"The student Name is {self.name} and got marks {self.marks}")



std1 = Student()
std2 = Student()

std1.set_details("Udit", 85)
std2.set_details("Omkar", 95)

std1.show_details()
std2.show_details()