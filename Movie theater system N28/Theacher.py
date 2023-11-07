from MovieTheacher import MovieTheater

class StandardTheater(MovieTheater):
    def __init__(self, location, seating_capacity):
        super().__init__(location, seating_capacity)

    def reserve_seats(self, showtime, num_seats):
        if num_seats <= showtime.available_seats:
            showtime.available_seats -= num_seats
            return True
        else:
            return False


class IMAXTheater(MovieTheater):
    def __init__(self, location, seating_capacity):
        super().__init__(location, seating_capacity)

    def reserve_seats(self, showtime, num_seats):
        if num_seats <= showtime.available_seats:
            showtime.available_seats -= num_seats
            return True
        else:
            return False
