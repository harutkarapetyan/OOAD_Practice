
class Rental:
    def __init__(self, customer, movie, duration):
        self.customer = customer
        self.movie = movie
        self.duration = duration

    def __str__(self):
        return f"Rental: {self.customer.name} rented '{self.movie.title}' for {self.duration} days."
