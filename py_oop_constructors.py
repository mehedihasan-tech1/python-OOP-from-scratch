class Car:
    def __init__(self, model, year, color, for_sale):
        self.model = model,
        self.year = year,
        self.color = color,
        self.for_sale = for_sale

    def auto_drive_mode(self):
        print(
            f"This car model no {self.model} {self.year} has auto drive mood")


car1 = Car("Audi", 2024, "black", False)
car2 = Car("Toyota", 2025, "black and red", False)
car3 = Car("Maclor", 2026, "navy blue", True)


print(car1.model)
print(car1.year)
car1.auto_drive_mode()
