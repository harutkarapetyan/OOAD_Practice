class Ride:
    def __init__(self, driver, passenger, destination):
        self.driver = driver
        self.passenger = passenger
        self.destination = destination
        self.fare = None
        self.completed = False
        self.driver_rating = None
        self.passenger_rating = None

    def accept_ride(self, driver):
        self.driver = driver

    def complete_ride(self):
        self.completed = True

    def rate_driver(self, rating):
        self.driver_rating = rating

    def rate_passenger(self, rating):
        self.passenger_rating = rating
