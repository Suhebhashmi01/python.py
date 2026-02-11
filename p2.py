class Animal:
    def sound(self):
        print("Some generic sound")

class Cat(Animal):
    def sound(self):
        print("Meow!")
a = Animal()
c = Cat()
a.sound()
c.sound()