from cars import ElectricCar, HybridCar
from Customer import Customer
from SalesPerson import Salesperson


if __name__ == "__main__":
    electric_car = ElectricCar("Tesla", "Model 3", 45000, 85)
    hybrid_car = HybridCar("Toyota", "Prius", 25000, 50)

    car_inventory = [electric_car, hybrid_car]

    customer1 = Customer("Alice", "alice@example.com")
    customer2 = Customer("Bob", "bob@example.com")

    salesperson = Salesperson("John", 0.05)  # 5% commission rate

    car_to_purchase = customer1.search_for_car(car_inventory, "Tesla", "Model 3")
    customer1.purchase_car(car_to_purchase, salesperson)

    salesperson.view_sales_history()