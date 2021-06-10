
from Person import Person

class Checker(Person):
    def __init__(self, code1 = None, name = None, email = None, phonenumber = None, contract = None, salary = None):
       
       super().__init__(code1=code1, name=name, email=email, phonenumber=phonenumber)
       self.contract = contract
       self.salary = salary