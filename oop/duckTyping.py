class Animal():
    is_alive = True

class Dog(Animal):
    def speak(self):
        print("Woof!")

class Cat(Animal):
    def speak(self):
        print("Meaow")

class Cow():
    def speak(self):
        print("Moo")

animals = [Dog(), Cat(), Cow()]

for animal in animals:
    animal.speak()
    print(Animal.is_alive)
