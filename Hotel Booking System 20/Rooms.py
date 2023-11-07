from abc import ABC, abstractmethod

# Abstract class for reservation operations
class ReservationOperation(ABC):
    @abstractmethod
    def book_room(self, reservation):
        pass

    @abstractmethod
    def view_reservation_history(self):
        pass

# Concrete classes for different types of rooms
class StandardRoom(ReservationOperation):
    def __init__(self, room_number, price, amenities):
        self.room_number = room_number
        self.price = price
        self.amenities = amenities

    def book_room(self, reservation):
        reservation.room = self

    def view_reservation_history(self):
        return f"Standard Room: Room {self.room_number}, Price: {self.price}"

class DeluxeRoom(ReservationOperation):
    def __init__(self, room_number, price, amenities):
        self.room_number = room_number
        self.price = price
        self.amenities = amenities

    def book_room(self, reservation):
        reservation.room = self

    def view_reservation_history(self):
        return f"Deluxe Room: Room {self.room_number}, Price: {self.price}"

