class Rental:
    def __init__(self, customer, car, duration, car_type):
        self.customer = customer
        self.car = car
        self.duration = duration
        self.car_type = car_type
        self.returned = False