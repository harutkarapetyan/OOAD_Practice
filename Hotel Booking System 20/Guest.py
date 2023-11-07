from validate_decorators import validate_email, validate_non_empty_string

class Guest:
    @validate_non_empty_string("name")
    @validate_email("contact_info")
    def __init__(self, name, contact_info):
        self.name = name
        self.contact_info = contact_info
        self.reservations = []

    def book_room(self, room, reservation):
        room.book_room(reservation)
        self.reservations.append(reservation)

    def view_reservation_history(self):
        print(f"Reservation history for Guest {self.name}:")
        for reservation in self.reservations:
            print("Reserved Room:")
            print(f"- {reservation.room.view_reservation_history()}")
            print(f"Reservation Dates: {reservation.dates}")
