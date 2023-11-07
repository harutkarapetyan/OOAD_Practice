from Menu import AppetizerMenu, EntreeMenu
from Customer import Customer
from Orders import Order

if __name__ == "__main__":
# Create menus
    appetizer_menu = AppetizerMenu()
    appetizer_menu.add_item("Salad", 6)
    appetizer_menu.add_item("Soup", 4)

    entree_menu = EntreeMenu()
    entree_menu.add_item("Burger", 10)
    entree_menu.add_item("Pizza", 12)

    # Create customers
    customer1 = Customer("John", "john@gmail.com")
    customer2 = Customer("Alice", "alice@gmail.com")

    # Place orders
    order1 = Order(customer1)
    order1.add_item(appetizer_menu.items[0])
    order1.add_item(entree_menu.items[1])

    order2 = Order(customer2)
    order2.add_item(entree_menu.items[0])

    # View order history
    customer1.view_order_history([order1])
    customer2.view_order_history([order2])