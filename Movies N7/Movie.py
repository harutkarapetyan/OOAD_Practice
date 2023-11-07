from abc import ABC, abstractmethod

# Abstract class for movies
class Movie(ABC):
    def __init__(self, title, genre, rating):
        self.title = title
        self.genre = genre
        self.rating = rating

    @abstractmethod
    def rent(self, customer, duration):
        pass

    @abstractmethod
    def return_movie(self, customer):
        pass

# Concrete classes for different types of movies
class ComedyMovie(Movie):
    def rent(self, customer, duration):
        print(f"{customer.name} has rented the comedy movie '{self.title}' for {duration} days.")

    def return_movie(self, customer):
        print(f"{customer.name} has returned the comedy movie '{self.title}'.")

class DramaMovie(Movie):
    def rent(self, customer, duration):
        print(f"{customer.name} has rented the drama movie '{self.title}' for {duration} days.")

    def return_movie(self, customer):
        print(f"{customer.name} has returned the drama movie '{self.title}'.")
