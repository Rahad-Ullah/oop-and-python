# class Engine:
#     def __init__(self):
#         pass

#     def start(self):
#         print("Engine started")

# class Driver:
#     def __init__(self):
#         pass

# class Car:
#     def __init__(self):
#         self.engine = Engine()
#         self.driver = Driver()

#     def start(self):
#         self.engine.start()

# toyota = Car()
# toyota.start() 


class CPU:
    def __init__(self, cores):
        self.cores = cores

class RAM:
    def __init__(self, size):
        self.size = size

class SSD:
    def __init__(self, capacity):
        self.capacity = capacity

class Computer:
    def __init__(self, cores, ram_size, ssd_capacity):
        self.cpu = CPU(cores)
        self.ram = RAM(ram_size)
        self.ssd = SSD(ssd_capacity)


mac = Computer(8, 16, 512)
print(mac.cpu.cores)
print(mac.ram.size)
print(mac.ssd.capacity)