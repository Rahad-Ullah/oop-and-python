# readonly -> you can't change the value
# getter -> get the value of a property using a method
# setter -> set the value of a private property using a method

class User:
    def __init__(self, name, age, money):
        self._name = name
        self._age = age
        self.__money = money

    @property
    def age(self):
        return self._age

    # getter
    @property
    def money(self):
        return self.__money

    # setter
    @money.setter
    def money(self, value):
        if value < 0:
            raise ValueError
        self.__money = value

samsu = User('samsu', 21, 1000)
print(samsu.age)
samsu.money = 100
print(samsu.money)