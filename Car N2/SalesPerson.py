from abc import ABC, abstractmethod
from validate_decorator import validate_non_empty_string, validate_positive_number


class AccountOperations(ABC):
    @abstractmethod
    def view_sales_history(self):
        pass


class Salesperson(AccountOperations):
    def __init__(self, name, commission_rate):
        self.name = name
        self.commission_rate = commission_rate
        self.sales_history = []

    def view_sales_history(self):
        print(f"Sales history for {self.name}:")
        for sale in self.sales_history:
            print(sale)

    def sell_car(self, car, customer):
        if car:
            sale_amount = car.price * (1 + self.commission_rate)
            self.sales_history.append(f"{customer.name} purchased a {car.make} {car.model} for ${sale_amount:.2f}")
            print(f"{customer.name} purchased a {car.make} {car.model} for ${sale_amount:.2f} (including commission).")
