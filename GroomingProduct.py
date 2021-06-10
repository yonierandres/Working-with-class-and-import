from Product import Product


from Product import Product

class GroomingProduct(Product):
    def __init__(self, code = None, name = None, price = None, iva = None, stock = None, createdate = None):
        super().__init__(code, name, price, iva, stock)
        self.createdate = createdate