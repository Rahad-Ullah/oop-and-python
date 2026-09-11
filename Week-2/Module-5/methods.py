class Phone:
    brand = 'iPhone'
    color = 'black'
    price = 1000
    features = ['camera', 'touch screen', 'speaker']

    def call(self):
        print('Calling...')
        return 'Call successful'

    def send_message(self, to, message):
        print(f'Sending message to {to}: {message}')
        return 'Message sent'

my_phone = Phone()
print(my_phone.brand)
print(my_phone.color)
print(my_phone.price)
print(my_phone.features)

my_phone.call()
my_phone.send_message('01234567890', 'Hello')

