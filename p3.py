class BankAccount:
    def __init__(self,owner,balence):
        self.owner=owner
        self.__balence=balence #private attributr

    def deposit(self,amount):
        self.__balence+=amount
    def get_balence(self):
        return self.__balence
    
acc = BankAccount("Alice",10000)
acc.deposit(5000)
print(acc.get_balence())
