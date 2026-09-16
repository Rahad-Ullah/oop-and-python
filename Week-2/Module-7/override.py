class Person:
    def __init__(self, name, age, gender, height, weight):
        self.name = name
        self.age = age
        self.gender = gender
        self.height = height
        self.weight = weight

    def eat(self):
        print(f"{self.name} is eating food")


class Cricketer(Person):
    def __init__(self, name, age, gender, height, weight, runs, wickets):
        super().__init__(name, age, gender, height, weight)
        self.runs = runs
        self.wickets = wickets

    def eat(self):  # override method
        print(f"{self.name} is eating food, but healthy food")

musfiq = Cricketer("Musfiq", 30, "Male", 5.8, 50, 5000, 100)
musfiq.eat()