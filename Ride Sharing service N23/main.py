from Passenger import Passenger
from Driver import Driver

if __name__ == "__main__":
    car_driver = Driver("Car Driver", "car_driver@example.com", "Car")
    moto_driver = Driver("Moto Driver", "moto_driver@example.com", "Motorcycle")
    passenger = Passenger("Passenger", "passenger@example.com")

    ride1 = car_driver.request_ride(passenger, "Work")
    ride1.fare = 20.0
    ride1.complete_ride()
    ride1.rate_driver(5)

    ride2 = moto_driver.request_ride(passenger, "Home")
    ride2.fare = 15.0
    ride2.complete_ride()
    ride2.rate_driver(4)

    print(f"{ride1.driver.name} was rated: {ride1.driver_rating}")
    print(f"{ride2.driver.name} was rated: {ride2.driver_rating}")



