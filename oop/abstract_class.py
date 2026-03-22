#abc stands for abstract base class

from abc import ABC, abstractmethod

class Vehicle(ABC):
    pass

    @abstractmethod
    def go(self):
        pass

    @abstractmethod
    def stop(self):
        pass

class Car(Vehicle):
    def go(self):
        print("you drive the Car")

    def stop(self):
        print("you stop the Car")

class Bike(Vehicle):
    def go(self):
        print("you ride the Bike")

    def stop(self):
        print("you stop the Bike")

car = Car()
bike = Bike()

car.go()
car.stop()

bike.go()
bike.stop()
