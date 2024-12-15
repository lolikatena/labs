class Vehicle:
    def __init__(self, make, model):
        self.make = make
        self.model = model

    def get_info(self):
        return f"Марка: {self.make}, Модель: {self.model}"

class Car(Vehicle):
    def __init__(self, make, model, fuel_type):
        super().__init__(make, model)  #вызов конструктора родительского класса
        self.fuel_type = fuel_type

    def get_info(self):
        return f"{super().get_info()}, Тип топлива: {self.fuel_type}"


vehicle = Vehicle("Chevrolet", "Comaro")
print(vehicle.get_info())

car = Car("Porsche", "911 Turbo S", "Спортивное топливо")
print(car.get_info())