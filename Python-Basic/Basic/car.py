class Car:
    def __init__(self, brand, model, year):
        self.brand = brand
        self.model = model
        self.year = year

    def show (self):
        return print(f"Car specs: {self.brand} - {self.model} - {self.year}")
