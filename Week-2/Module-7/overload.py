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

    def __add__(self, other):  # overload + operator
        return self.runs + other.runs

    def __sub__(self, other):  # overload - operator
        return self.runs - other.runs

    def __mul__(self, other):  # overload * operator
        return self.runs * other.runs

    def __len__(self):  # overload len
        return self.wickets

    def __gt__(self, other):    # overload > operator
        return self.runs > other.runs

musfiq = Cricketer("Musfiq", 30, "Male", 5.8, 50, 5000, 100)
tamim = Cricketer("Tamim", 30, "Male", 5.8, 50, 5000, 100)

print(musfiq + tamim)
print(musfiq - tamim)
print(musfiq * tamim)
print(len(musfiq))
print(musfiq > tamim)
