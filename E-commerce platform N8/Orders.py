class Order:
    def __init__(self, customer, products):
        self.customer = customer
        self.products = products
        self.total_price = sum(product.price for product in products)

    def __str__(self):
        product_names = [str(product) for product in self.products]
        return f"Order: {self.customer.name} ordered {', '.join(product_names)} for a total of ${self.total_price}."
