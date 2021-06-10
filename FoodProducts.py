
from Product import Product

class FoodProducts(Product):
    
    def __init__(self, code = None, name = None, price = None, iva = None, stock = None, duedate = None):
        super().__init__(code, name, price, iva, stock)
        self.duedate = duedate