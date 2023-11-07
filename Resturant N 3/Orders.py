from validate_decorators import validate_non_empty_string, validate_email
 
class Order:
    def __init__(self, customer):
        self.customer = customer
        self.items = []
        self.total_price = 0

    def add_item(self, item, quantity=1):
        self.items.extend([item] * quantity)
        self.total_price += item.price * quantity

    def display_order(self):
        print("Order for", self.customer.name)
        for item in self.items:
            print(item)
        print(f"Total Price: ${self.total_price:.2f}")
       