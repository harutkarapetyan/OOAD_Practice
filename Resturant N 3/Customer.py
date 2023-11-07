from abc import ABC, abstractmethod
from validate_decorators import validate_non_empty_string, validate_email
                   
class Customer:
    @validate_non_empty_string("name")
    @validate_email("contact_info")
    def __init__(self, name, contact_info):
        self.name = name
        self.contact_info = contact_info

    def view_order_history(self, order_history):
        print(f"Order history for {self.name}:")
        for order in order_history:
            order.display_order()
            print('-' * 30)
            
    def view_menu(self, menu):
        return menu