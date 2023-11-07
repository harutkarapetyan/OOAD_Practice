from transactions import LuxuryCar, EconomyCar
from Rentals import Rental
from Cars import Car
from Customers import Customer




if __name__ == "__main__":

    customer1 = Customer("Customer1", "customer1@examplegmail.com")
    customer2 = Customer("Customer2", "customer2@examplegmail.com")

    luxury_car = LuxuryCar()
    economy_car = EconomyCar()

    car1 = Car("Mercedes", "S-Class", 150)
    car2 = Car("Toyota", "Camry", 80)

    customer1.rent_car(luxury_car, car1, 7)
    customer2.rent_car(economy_car, car2, 5)
    customer1.rent_car(economy_car, car2, 3)

    customer1.return_car(customer1.rentals[0])
    customer2.return_car(customer2.rentals[0])

    customer1.view_rental_history()
    customer2.view_rental_history()


    
