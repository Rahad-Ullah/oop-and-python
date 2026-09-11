class Shop:
    name = 'My Shop'   # class attribute : shared by all instances

    def __init__(self, buyer_name):
        self.buyer_name = buyer_name
        self.cart = []  # instance attribute : unique to each instance

    def add_to_cart(self, item):
        self.cart.append(item)

my_shop = Shop('John')
my_shop.add_to_cart('apple')
my_shop.add_to_cart('banana')
my_shop.add_to_cart('orange')

print(my_shop.buyer_name)
print(my_shop.cart)

my_shop2 = Shop('Rahad')
my_shop2.add_to_cart('pineapple')
my_shop2.add_to_cart('banana')
my_shop2.add_to_cart('jackfruit')

print(my_shop2.buyer_name)
print(my_shop2.cart)