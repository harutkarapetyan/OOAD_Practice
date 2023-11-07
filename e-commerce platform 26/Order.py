
class Order:
    order_counter = 0

    def __init__(self, customer, products, total_price):
        Order.order_counter += 1
        self.order_id = Order.order_counter
        self.customer = customer
        self.products = products
        self.total_price = total_price
