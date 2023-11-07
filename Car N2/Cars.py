from validate_decorator import validate_non_empty_string, validate_positive_number
from abc import ABC, abstractmethod


class Cars(ABC):
    @validate_non_empty_string("make", 1)
    @validate_non_empty_string("model", 2)
    @validate_positive_number("price", 3)
    def __init__(self, make, model, price):
        self.make = make
        self.model = model
        self.price = price

    @abstractmethod
    def show_car_info(self):
        pass


class ElectricCar(Cars):
    @validate_positive_number("battery_capacity", 4)
    def __init__(self, make, model, price, battery_capacity):
        super().__init__(make, model, price)
        self.battery_capacity = battery_capacity

    def show_car_info(self):
        return f"Electric Car: {self.make} {self.model}, Price: ${self.price}, Battery Capacity: {self.battery_capacity} kWh"


class HybridCar(Cars):
    def __init__(self, make, model, price, gas_mileage):
        super().__init__(make, model, price)
        self.gas_mileage = gas_mileage

    def show_car_info(self):
        return f"Hybrid Car: {self.make} {self.model}, Price: ${self.price}, Gas Mileage: {self.gas_mileage} mpg."
