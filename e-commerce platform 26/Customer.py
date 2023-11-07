from Order import Order
from Product import ECommerceOperation
from validate_decorators import validate_email, validate_non_empty_string

class Customer(ECommerceOperation):
    @validate_non_empty_string("name")
    @validate_email("contact_info")
    def __init__(self, name, contact_info):
        self.name = name
        self.contact_info = contact_info
        self.past_orders = []

    def browse_products(self):
        print(f"{self.name} is browsing products on the e-commerce platform.")

    def purchase_products(self, products):
        total_price = sum(product.price for product in products)
        order = Order(self, products, total_price)
        self.past_orders.append(order)
        print(f"{self.name} has made a purchase. Total cost: ${total_price}")

    def view_past_orders(self):
        for order in self.past_orders:
            print(f"Order ID: {order.order_id}, Total Price: ${order.total_price}")

    def leave_review(self, product, review):
        print(f"{self.name} left a review for {product.name}: {review}")

