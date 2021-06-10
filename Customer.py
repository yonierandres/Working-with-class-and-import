
from Person import Person

class Customer(Person):
    def __init__(self, code1 = None, name = None, email = None, phonenumber = None, category = None):
       
       super().__init__(code1=code1, name=name, email=email, phonenumber=phonenumber)
       self.category = category
       