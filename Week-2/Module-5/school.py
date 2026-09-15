class Student:
    def __init__(self, name, current_class, id):
        self.name = name
        self.current_class = current_class
        self.id = id

    def __repr__(self):
        return f"Name: {self.name}, Class: {self.current_class}, ID: {self.id}"

class Teacher:
    def __init__(self, name, subject, id):
        self.name = name
        self.subject = subject
        self.id = id

    def __repr__(self):
        return f"Name: {self.name}, Subject: {self.subject}, ID: {self.id}"

class School:
    def __init__(self, name, address):
        self.name = name
        self.address = address
        self.teachers = []
        self.students = []

    def __repr__(self):
        print(f"Welcome to {self.name}, {self.address}")
        print("---------Our Teachers:---------")
        for teacher in self.teachers:
            print(teacher)
        print("---------Our Students:---------")
        for student in self.students:
            print(student)
        return "All done"

    def add_teacher(self, name, subject):
        id = len(self.teachers) + 1
        teacher = Teacher(name, subject, id)
        self.teachers.append(teacher)

    def enroll(self, name, current_class):
        id = len(self.students) + 1
        student = Student(name, current_class, id)
        self.students.append(student)

phitron = School("Phitron", "Dhaka")

phitron.add_teacher("Jhankar Mahbub", "Python")

phitron.enroll("Rahad Ullah", "Python")
phitron.enroll("Suhag", "C++")
phitron.enroll("Huzaifa", "C")

print(phitron)

