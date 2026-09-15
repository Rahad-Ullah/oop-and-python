class Shopping:
    def __init__(self, name):
        self.name = name
        self.cart = []

    def add_to_cart(self, item, price, quantity):
        product = {'item': item, 'price': price, 'quantity': quantity}
        self.cart.append(product)

    def checkout(self, amount):
        total = 0
        for item in self.cart:
            total += item['price'] * item['quantity']
        if total > amount:
            return 'Insufficient balance'
        else:
            return 'Checkout successful. Change: {}'.format(amount - total)


shop = Shopping('John Smith')
shop.add_to_cart('iPhone', 1000, 1)
shop.add_to_cart('Macbook Pro', 2000, 1)
print(shop.checkout(3000))