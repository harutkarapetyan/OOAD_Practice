from validate_decorator import validate_non_empty_string, validate_email


class Customer:
    @validate_non_empty_string("name", 1)
    @validate_email("contact_info", 2)
    def __init__(self, name, contact_info):
        self.name = name
        self.contact_info = contact_info

    def search_for_car(self, car_inventory, make, model):
        for car in car_inventory:
            if car.make == make and car.model == model:
                return car
        return None

    def purchase_car(self, car, salesperson):
        if car:
            print(f"{self.name} purchased a {car.make} {car.model} from {salesperson.name}.")
        else:
            print(f"Car not found in the inventory.")
