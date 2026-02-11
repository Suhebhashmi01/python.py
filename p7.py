class Mobile:
    def __init__(self,price):
        self.__price= price
    def display_price(self):
        print("Mobile price is",self.__price)

s1=Mobile(25000)
s1.display_price()