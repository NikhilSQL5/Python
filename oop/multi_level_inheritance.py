class Vehicle:
    def __init__(self, brand, name):
        self.brand = brand
        self.name = name     

class Petrol(Vehicle):
    def use_petrol(self):
        print(f"{self.name} use Petrol")

class Electric(Vehicle):
    def use_electricity(self):
        print(f"{self.name} use Electricity")


class Elevate(Petrol):
    def spec(self):
        print("This is 2026 petrol car with 20kmpl fuel efficiency")
        print("best petrol car")

class Jazz(Electric):
   def spec(self):
        print("This is 2026 Electric car with 300km+ range")
        print("best Electric car")

class HondaCity(Petrol, Electric):
    def spec(self):
        print("This is 2026 hybrid car with 35kmpl fuel efficiency")
        print("best Hybrid car")

elevate = Elevate("Honda", "Elevate")
elevate.use_petrol()
elevate.spec()

jazz = Jazz("Honda", "Jazz")
jazz.use_electricity()

city = HondaCity("Honda", "HondaCity")
city.use_petrol()
city.use_electricity()
city.spec()
