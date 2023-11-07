from Customer import Customer
from Product import ElectronicsProduct, ClothingProduct



if __name__ == "__main__":
    customer1 = Customer("Alice", "alice@examplegmail.com")

    laptop = ElectronicsProduct("Laptop", "High-performance laptop", 1000, True, "Dell")
    t_shirt = ClothingProduct("T-shirt", "Cotton t-shirt", 20, True, "M", "Blue")

    customer1.browse_products()

    customer1.purchase_products([laptop, t_shirt])

    customer1.view_past_orders()

    customer1.leave_review(laptop, "Great laptop for work!")

