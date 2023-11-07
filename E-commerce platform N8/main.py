from Customers import Customer
from Products import ElectronicsProduct, ClothingProduct

if __name__ == "__main__":

    customer1 = Customer("Alice", "alice@examplegmail.com")
    customer2 = Customer("Bob", "bob@examplegmail.com")

    electronics_product = ElectronicsProduct("Laptop", 1000, "Powerful laptop for work and gaming")
    clothing_product = ClothingProduct("T-shirt", 20, "Comfortable cotton t-shirt")

    customer1.search_and_purchase(electronics_product)
    customer2.search_and_purchase(clothing_product)

    customer1.view_order_history()
    customer2.view_order_history()

    electronics_product.leave_review(customer1, "Great laptop for gaming!")
    clothing_product.leave_review(customer2, "Comfortable and stylish t-shirt.")

