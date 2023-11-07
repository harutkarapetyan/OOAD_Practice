from abc import ABC, abstractmethod
from validate_decorators import validate_non_empty_string, validate_positive_number
# Abstract class for products
class Product(ABC):
    @validate_positive_number("price")
    @validate_non_empty_string("name")
    @validate_non_empty_string("description")
    
    def __init__(self, name, price, description):
        self.name = name
        self.price = price
        self.description = description

    @abstractmethod
    def purchase(self, customer):
        pass

    @abstractmethod
    def leave_review(self, customer, review):
        pass
    
    def __str__(self):
        return self.name

# Concrete classes for different types of products
class ElectronicsProduct(Product):
    def purchase(self, customer):
        print(f"{customer.name} purchased the electronics product: {self.name}")

    def leave_review(self, customer, review):
        print(f"{customer.name} left a review for the electronics product {self.name}: {review}")

class ClothingProduct(Product):
    def purchase(self, customer):
        print(f"{customer.name} purchased the clothing product: {self.name}")

    def leave_review(self, customer, review):
        print(f"{customer.name} left a review for the clothing product {self.name}: {review}")

