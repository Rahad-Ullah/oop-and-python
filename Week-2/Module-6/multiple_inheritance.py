class Family:
    def __init__(self, name, address):
        self.name = name
        self.address = address

class School:
    def __init__(self, level, roll):
        self.level = level
        self.roll = roll

class Sports:
    def __init__(self, game):
        self.game = game

class Student(Family, School, Sports):
    def __init__(self, name, address, level, roll, game):
        Family.__init__(self , name, address)
        School.__init__(self, level, roll)
        Sports.__init__(self, game)

    def __repr__(self):
        return f"Name: {self.name}, Address: {self.address}, Level: {self.level}, Roll: {self.roll}, Game: {self.game}"


student = Student("John", "123 Main St", "High School", "12B", "Football")
print(student)
