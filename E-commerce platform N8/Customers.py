from validate_decorators import validate_email, validate_non_empty_string

class Customer:
    @validate_non_empty_string("name")
    @validate_email("contact_info")
    def __init__(self, name, contact_info):
        self.name = name
        self.contact_info = contact_info
        self.order_history = []

    def search_and_purchase(self, product):
        product.purchase(self)
        self.order_history.append(product)

    def view_order_history(self):
        print(f"Order history for {self.name}:")
        for order in self.order_history:
            print(order)