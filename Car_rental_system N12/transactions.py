# Abstract class for rental operations
from abc import ABC, abstractmethod
from Rentals import Rental
class RentalOperation(ABC):
    @abstractmethod
    def rent_car(self, customer, car, duration):
        pass

    @abstractmethod
    def return_car(self, rental):
        pass

# Concrete classes for different types of cars
class LuxuryCar(RentalOperation):
    def __str__(self):
        return "Luxury"

    def rent_car(self, customer, car, duration):
        rental = Rental(customer, car, duration, self)
        return rental

    def return_car(self, rental):
        rental.returned = True

class EconomyCar(RentalOperation):
    def __str__(self):
        return "Economy"

    def rent_car(self, customer, car, duration):
        rental = Rental(customer, car, duration, self)
        return rental

    def return_car(self, rental):
        rental.returned = True
