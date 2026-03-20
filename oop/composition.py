class Engine:
    def __init__(self, hp, cylinder, type):
        self.hp = hp
        self.cylinder = cylinder
        self.type = type

class Wheel:
    def __init__(self, size, type):
        self.size = size
        self.type = type

class Car:
    def __init__(self, brand, model, type, hp, wheel_size):
        self.brand = brand
        self.model = model
        self.type = type
        
        # FIX: pass all required arguments
        self.power = Engine(hp, 4, "petrol")
        self.wheels = Wheel(wheel_size, "alloy")
    
    def display_car(self):
        return f"{self.brand} {self.model} {self.power.hp}HP {self.wheels.size}inch"

car = Car("TATA", "Punch", "micro-SUV", 200, 17)

print(car.display_car())
