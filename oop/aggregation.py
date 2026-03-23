class Phone_Store:
    def __init__(self,name):
        self.name = name
        self.phones = []
    
    def add_phone(self, phone):
        self.phones.append(phone)

    def list_phone(self):
        return [f"{phone.model} by {phone.brand}"for phone in self.phones]


class Phone:
    def __init__(self,brand,model):
        self.brand = brand
        self.model = model
    
store = Phone_Store("Max Sales")

phone1 = Phone("Apple", "iphone 17Pro")
phone2 = Phone("Samsung", "Galaxy s26")
phone3 = Phone("Google", "Pixel 10pro")

store.add_phone(phone1)
store.add_phone(phone2)
store.add_phone(phone3)

print(store.name)

for phone in store.list_phone():
    print(phone)
