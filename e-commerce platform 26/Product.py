from abc import ABC, abstractmethod

# Abstract class for e-commerce operations
class ECommerceOperation(ABC):
    @abstractmethod
    def browse_products(self):
        pass

    @abstractmethod
    def purchase_products(self, customer, products):
        pass

    @abstractmethod
    def view_past_orders(self, customer):
        pass

    @abstractmethod
    def leave_review(self, product, customer, review):
        pass

# Concrete class for products
class Product:
    def __init__(self, name, description, price, availability):
        self.name = name
        self.description = description
        self.price = price
        self.availability = availability

# Concrete classes for different types of products (electronics and clothing)
class ElectronicsProduct(Product):
    def __init__(self, name, description, price, availability, brand):
        super().__init__(name, description, price, availability)
        self.brand = brand

class ClothingProduct(Product):
    def __init__(self, name, description, price, availability, size, color):
        super().__init__(name, description, price, availability)
        self.size = size
        self.color = color