class Calculator:
    def add(self, a, b):
        return a + b

    def subtract(self, a, b):
        return a - b

    def multiply(self, a, b):
        return a * b

    def divide(self, a, b):
        return a / b

    def mod(self, a, b):
        return a % b

my_calculator = Calculator()

print(my_calculator.add(10, 5))
print(my_calculator.subtract(10, 5))
print(my_calculator.multiply(10, 5))
print(my_calculator.divide(10, 5))
print(my_calculator.mod(10, 5))