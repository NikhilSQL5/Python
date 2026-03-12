class Car:

    brand = "Toyota"

    def __init__(self, color, year): 
        self.color = color
        self.year = year

class Fortuner(Car):
    def __init__(self, engine, price, color, year):
        self.engine = engine
        self.price = price
        super().__init__(color,year)

class Inova(Car):
    def __init__(self, engine, price, color, year):
        self.engine = engine
        self.price = price
        super().__init__(color,year)

class Etios(Car):
    def __init__(self, engine, price, color, year):
        self.engine = engine
        self.price = price
        super().__init__(color,year)

etios = Etios("2.0L","18Lakh","brown","2026")
inova = Inova("2.5L","35Lakh","red","2026")
fortuner = Fortuner("2.5L","40Lakh","black","2026")

print(etios.color)
print(inova.color)
print(fortuner.color)

print("below is available cars in showroom")
print(f"the spec of Inova is Engine = {inova.engine}, price of Inova = {inova.price}, color of Inova = {inova.color}, Manufacture = {inova.year}")
print(f"the spec of Fortuner is Engine = {fortuner.engine}, price of Fortuner = {fortuner.price}, color of Fortuner = {fortuner.color}, Manufacture = {fortuner.year}")
print(f"the spec of Etios is Engine = {etios.engine}, price of Etios = {etios.price}, color of Etios = {etios.color}, Manufacture = {etios.year}")
