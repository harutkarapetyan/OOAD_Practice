from validate_decorators import validate_email, validate_non_empty_string

class Customer:
    @validate_non_empty_string("name")
    @validate_email("contact_info")
    
    def __init__(self, name, contact_info):
        self.name = name
        self.contact_info = contact_info
        self.rental_history = []

    def rent_movie(self, movie, duration):
        rental = movie.rent(self, duration)
        self.rental_history.append(rental)

    def view_rental_history(self):
        print(f"Rental history for {self.name}:")
        for rental in self.rental_history:
            print(rental)
