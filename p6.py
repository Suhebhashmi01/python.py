class Employee:
    def __init__(self,salary):
        self.__salary= salary
    def display_salary(self):
        print("salary",self.__salary)
    def increase_salary(self,amount):
        self.__salary += amount
        print("salary increased by",amount)

s1=Employee(15000)
s1.display_salary()
s1.increase_salary(5000)
s1.display_salary()