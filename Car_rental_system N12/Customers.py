from validate_decorators import validate_email, validate_non_empty_string

class Customer:
    @validate_non_empty_string("name")
    @validate_email("contact_info")
    def __init__(self, name, contact_info):
        self.name = name
        self.contact_info = contact_info
        self.rentals = []

    def rent_car(self, car_type, car, duration):
        rental = car_type.rent_car(self, car, duration)
        self.rentals.append(rental)

    def return_car(self, rental):
        rental.car_type.return_car(rental)

    def view_rental_history(self):
        print(f"Rental history for {self.name}:")
        for rental in self.rentals:
            status = "Returned" if rental.returned else "Not Returned"
            print(f"- {rental.car.make} {rental.car.model} ({rental.car_type}): {status}")
