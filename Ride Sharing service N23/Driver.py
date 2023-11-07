from validate_decorators import validate_email, validate_non_empty_string
from RideSharingoperation import RideSharingOperation
from Ride import Ride

class Driver(RideSharingOperation):
    @validate_non_empty_string("name")
    @validate_email("contact_info")
    def __init__(self, name, contact_info, vehicle):
        self.name = name
        self.contact_info = contact_info
        self.vehicle = vehicle

    def request_ride(self, passenger, destination):
        ride = Ride(self, passenger, destination)
        passenger.request_ride(ride)
        return ride

    def accept_ride(self, ride):
        ride.accept_ride(self)

    def complete_ride(self, ride):
        ride.complete_ride()
