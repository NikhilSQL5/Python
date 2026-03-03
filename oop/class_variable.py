class Car:

    brand = "Honda"
    
    total_cars = 0

    def __init__ (self, name, colour, fuel_type):
        self.name = name
        self.colour = colour
        self.fuel_type = fuel_type
        Car.total_cars += 1
    
    def spec(self):
        print(f"Model = {self.name}, Colour = {self.colour}, Fuel Type = {self.fuel_type}")

HondaCity = Car("HondaCity", "Blue", "Petrol")
Elevate = Car("Elevate", "Blue", "Petrol")
Jazz = Car("Jazz", "Blue", "Electic")
eHEV = Car("HondaCity eHev", "Blue", "Petrol + Electric")

HondaCity.spec()
print(f"Total record's of the car {Car.total_cars}")
