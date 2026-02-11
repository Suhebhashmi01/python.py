class Student:
    def __init__(self, marks):
        self.__marks = marks   # private variable

    def display_marks(self):
        print("Marks:", self.__marks)


# Creating object of the class
s1 = Student(85)

# Calling method to display marks
s1.display_marks()
