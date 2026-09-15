# Ena Poribohon

class Company:
    def __init__(self, name, address):
        self.name = name
        self.address = address
        self.bus = []
        self.routes = []
        self.drivers = []
        self.vehicles = []
        self.counters = []
        self.managers = []
        self.supervisors = []


class Driver:
    def __init__(self, name, id, license, age):
        self.name = name
        self.id = id
        self.license = license
        self.age = age


class Vehicle:
    def __init__(self, name, id, type, capacity):
        self.name = name
        self.id = id
        self.type = type
        self.capacity = capacity

class Counter:
    def __init__(self, name, id, location):
        self.name = name
        self.id = id
        self.location = location

