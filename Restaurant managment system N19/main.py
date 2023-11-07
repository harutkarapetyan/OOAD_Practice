from Customer import Customer
from Order import Order
from Meniu import Appetizer, Entree

if __name__ == "__main__":

    customer1 = Customer("Customer1", "customer1@examplegmail.com")

    appetizer1 = Appetizer("Salad", 12.5, ["Lettuce", "Tomato", "Cucumber"])
    entree1 = Entree("Steak", 25.6, ["Steak", "Potatoes", "Asparagus"])

    order1 = Order(customer1)
    customer1.place_order(appetizer1, order1)
    customer1.place_order(entree1, order1)

    customer1.view_order_history()

    
