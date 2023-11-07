from Guest import Guest
from Reservation import Reservation
from Rooms import StandardRoom, DeluxeRoom 


if __name__ == "__main__":
    
    guest1 = Guest("Guest1", "guest1@examplegmail.com")

    standard_room1 = StandardRoom("101", 92, ["TV", "Bathroom"])
    deluxe_room1 = DeluxeRoom("201", 159, ["TV", "Mini-Bar"])

    reservation1 = Reservation(guest1, "2023-01-15 to 2023-01-20")
    reservation2 = Reservation(guest1, "2023-02-10 to 2023-02-15")

    guest1.book_room(standard_room1, reservation1)
    guest1.book_room(deluxe_room1, reservation2)

    guest1.view_reservation_history()

