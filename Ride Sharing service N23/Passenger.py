from validate_decorators import validate_email, validate_non_empty_string

class Passenger:
    @validate_non_empty_string("name")
    @validate_email("contact_info")
    def __init__(self, name, contact_info):
        self.name = name
        self.contact_info = contact_info
        self.requested_rides = []

    def request_ride(self, ride):
        self.requested_rides.append(ride)
