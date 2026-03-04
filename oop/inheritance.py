class Animal:
    def __init__(self,name):
        self.name = name
    
    def eat(self):
        print(f"{self.name} is eating")
    
    def sleep(self):
        print(f"{self.name} is sleeping")

class Cat(Animal):

    def sound(self):
        print(f"{self.name} is cat and it can meow")

    def eat(self):
        print(f"{self.name} eating pizza") #override

cat = Cat("silvester")

cat.eat()
cat.sound()
