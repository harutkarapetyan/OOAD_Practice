from validate_decorators import validate_email, validate_non_empty_string

class Customer:
    @validate_non_empty_string("name")
    @validate_email("contact_info")
    def __init__(self, name, contact_info):
        self.name = name
        self.contact_info = contact_info
        self.orders = []

    def place_order(self, menu_item, order):
        menu_item.place_order(order)
        self.orders.append(order)

    def view_order_history(self):
        print(f"Order history for Customer {self.name}:")
        for order in self.orders:
            print("Order Items:")
            for item in order.menu_items:
                print(f"- {item.view_order_history()}")
            print(f"Total Price: {order.total_price}")
