class Phone:
    brand = 'iPhone'
    color = 'black'
    price = 1000

    def __init__(self, brand, color, price):
        self.brand = brand
        self.color = color
        self.price = price

    def call(self):
        print('Calling...')

    def send_message(self, to, message):
        print(f'Sending message to {to}: {message}')
        return 'Message sent'


my_phone = Phone('iPhone', 'black', 1000)
her_phone = Phone('Samsung', 'white', 2000)

print(my_phone.brand)
print(my_phone.color)
print(my_phone.price)

print(her_phone.brand)
print(her_phone.color)
print(her_phone.price)