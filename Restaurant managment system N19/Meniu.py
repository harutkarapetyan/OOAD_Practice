from abc import ABC, abstractmethod

# Abstract class for order operations
class OrderOperation(ABC):
    @abstractmethod
    def place_order(self, order):
        pass

    @abstractmethod
    def view_order_history(self):
        pass

# Concrete classes for different types of menu items
class Appetizer(OrderOperation):
    def __init__(self, name, price, ingredients):
        self.name = name
        self.price = price
        self.ingredients = ingredients

    def place_order(self, order):
        order.menu_items.append(self)
        order.total_price += self.price

    def view_order_history(self):
        return f"Appetizer: {self.name}, Price: {self.price}"

class Entree(OrderOperation):
    def __init__(self, name, price, ingredients):
        self.name = name
        self.price = price
        self.ingredients = ingredients

    def place_order(self, order):
        order.menu_items.append(self)
        order.total_price += self.price

    def view_order_history(self):
        return f"Entree: {self.name}, Price: {self.price}"

