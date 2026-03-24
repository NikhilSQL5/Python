class Car:
    def __init__(self, model, year, for_sale):
        self.model = model
        self.year = year
        self.for_sale = for_sale
    
    def drive(self):
        print(f"you drive {self.model} of {self.year} year model")
    
    def stop(self):
        print("you stop the car")
    
    def spec(self):
        print(f"model {self.model} year {self.year} for sale {self.for_sale}")

verna = Car("Verna", 2025, True)
virtus = Car("Virtus", 2026, True)
elevate = Car("Elevate",2025, False)

virtus.drive()
print(verna.model)
print(verna.for_sale)

verna.spec()
