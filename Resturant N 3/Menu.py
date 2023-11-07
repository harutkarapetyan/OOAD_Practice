from validate_decorators import validate_non_empty_string, validate_positive_number
from abc import ABC, abstractmethod

class Menu(ABC):
    def __init__(self):
        self.items = []

    @abstractmethod
    def add_item(self, name, price):
        pass

    def display_menu(self):
        for item in self.items:
            print(item)

class MenuItem:
    @validate_non_empty_string('name')
    @validate_positive_number('price')
    def __init__(self, name, price):
        self.name = name
        self.price = price

    def __str__(self):
        return f"{self.name} - ${self.price:.2f}"

class Dish(MenuItem):
    def __init__(self, name, price, category):
        super().__init__(name, price)
        self.category = category

class AppetizerMenu(Menu):
    
    def add_item(self, name, price):
        appetizer = Dish(name, price, 'Appetizer')
        self.items.append(appetizer)

class EntreeMenu(Menu):
    def add_item(self, name, price):
        entree = Dish(name, price, 'Entree')
        self.items.append(entree)
