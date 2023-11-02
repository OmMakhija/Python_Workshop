class dog:
    def __init__(self, name):
        self.name=name
dog1=dog("buddy")
print(dog1.name)
class car:
    def __init__(self,make,model):
        self.make=make
        self.model=model
car1=car("Toyota","Camry")
car2=car("Honda","Civic")
print(car1.make,car1.model)
print(car2.make,car2.model)
class BankAccount:
    def __init__(self,account_number,balance):
        self._account_number=account_number
        self.__balance=balance
    def get_balance(self):
        return self.__balance
    
account1=BankAccount("12345",1000)
print(account1._account_number)
print(account1.get_balance())

