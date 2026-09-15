# base class / parent class = common attributes + common methods
class Device:
    def __init__(self, brand, model, price, color) -> None:
        self.brand = brand
        self.model = model
        self.price = price
        self.color = color

    def run(self):
        print(f"Running {self.brand} {self.model}")


# derived class / child class = unique attributes + unique methods
class Laptop(Device):
    def __init__(self, brand, model, price, color, memory, processor) -> None:
        super().__init__(brand, model, price, color)
        self.memory = memory
        self.processor = processor

    def __repr__(self):
        return f"Brand: {self.brand}, Model: {self.model}, Price: {self.price}, Color: {self.color}, Memory: {self.memory}, Processor: {self.processor}"

class Phone(Device):
    def __init__(self, brand, model, price, color, memory, processor, dual_sim, camera) -> None:
        super().__init__(brand, model, price, color)
        self.memory = memory
        self.processor = processor
        self.dual_sim = dual_sim
        self.camera = camera

    def __repr__(self):
        return f"Brand: {self.brand}, Model: {self.model}, Price: {self.price}, Color: {self.color}, Memory: {self.memory}, Processor: {self.processor}, Dual Sim: {self.dual_sim}, Camera: {self.camera}"

    def phone_call(self, number):
        print(f"Calling {number}")

    def send_message(self, number, message):
        print(f"Sending message to {number}: {message}")


class Camera(Device):
    def __init__(self, brand, model, price, color, resolution, lens) -> None:
        super().__init__(brand, model, price, color)
        self.resolution = resolution
        self.lens = lens

    def __repr__(self):
        return f"Brand: {self.brand}, Model: {self.model}, Price: {self.price}, Color: {self.color}, Resolution: {self.resolution}, Lens: {self.lens}"

    def take_photo(self):
        print(f"Taking photo with {self.brand} {self.model}")

    def record_video(self):
        print(f"Recording video with {self.brand} {self.model}")


phone = Phone( 'iPhone', 'X', 1000, 'black', '20GB', 'Octacore A53', True, '16MP')
print(phone)

camera = Camera('Canon', 'EOS 5D', 5000, 'black', '4K', 'EF-S 18-55mm')
print(camera)