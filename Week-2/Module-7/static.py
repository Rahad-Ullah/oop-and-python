class Shopping:
    cart = []   # class/static attribute : same for all instances

    def __init__(self, name):
        self.name = name

    def purchase(self, item):   # class method: must pass self class
        self.cart.append(item)

    @staticmethod
    def view_product(item):     # static method: does not need self class, can be called directly from class
        print('View products:', item)

jamuna = Shopping('Jamuna')
jamuna.purchase('iPhone')

Shopping.view_product('Macbook Pro')