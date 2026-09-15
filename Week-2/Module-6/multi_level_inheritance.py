# base class / parent class = common attributes + common methods
class Vehicle:
    def __init__(self, name, model, type, price):
        self.name = name
        self.model = model
        self.type = type
        self.price = price

    def __repr__(self):
        return f"Name: {self.name}, Model: {self.model}, Type: {self.type}, Price: {self.price}"
        
class Bus(Vehicle):
    def __init__(self, name, model, type, price, route, driver, seats):
        super().__init__(name, model, type, price)
        self.route = route
        self.driver = driver
        self.seats = seats

class Truck(Vehicle):
    def __init__(self, name, model, type, price, route, driver, capacity):
        super().__init__(name, model, type, price)
        self.route = route
        self.driver = driver
        self.capacity = capacity

class PickupTruck(Truck):
    def __init__(self, name, model, type, price, route, driver, capacity, bed_length, wheelbase):
        super().__init__(name, model, type, price, route, driver, capacity)
        self.bed_length = bed_length
        self.wheelbase = wheelbase


class AcBus(Bus):
    def __init__(self, name, model, type, price, route, driver, seats, ac, ticket_price):
        super().__init__(name, model, type, price, route, driver, seats)
        self.ac = ac
        self.ticket_price = ticket_price

    def __repr__(self):
        return super().__repr__()


green_line = AcBus("Green Line", "1234", "Bus", 10000, "Green Line", "John Doe", 30, True, 5)
print(green_line)