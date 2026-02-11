class Employee:
    def __init__(self,salary):
        self.__salary= salary
    def display_salary(self):
        print("salary",self.__salary)

s1=Employee(15000)
s1.display_salary()