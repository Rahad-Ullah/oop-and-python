# poly -> many, morph -> shape

class Animal:
    def __init__(self, name):
        self.name = name

    def make_sound(self):   # act differently for different objects
        pass


class Cat(Animal):
    def __init__(self, name):
        super().__init__(name)

    def make_sound(self):
        print("meow")

class Dog(Animal):
    def __init__(self, name):
        super().__init__(name)

    def make_sound(self):
        print("bark")

class Goat(Animal):
    def __init__(self, name):
        super().__init__(name)

    def make_sound(self):
        print("mee mee")


tom = Cat("Tom")
tom.make_sound()

rex = Dog("Rex")
rex.make_sound()

mess = Goat("L Messi")
mess.make_sound()

