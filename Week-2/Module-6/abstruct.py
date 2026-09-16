from abc import ABC, abstractmethod
# abc -> abstract base class
class Animal(ABC):
    def __init__(self, name):
        self.name = name

    @abstractmethod
    def eat(self):  # abstract method -> must be redefine in child class
        # hidden implementation details
        pass

    def sleep(self):    # non-abstract method -> can be used in child class, no need to be redefined
        pass

class Monkey(Animal):
    def __init__(self, name):
        super().__init__(name)

    def eat(self):
        print(f"{self.name} is eating banana")

    def sleep(self):
        print(f"{self.name} is sleeping")

ponkey = Monkey("Ponkey")
ponkey.eat()
ponkey.sleep()