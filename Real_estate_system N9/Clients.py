
class Client:
    def __init__(self, name, contact_info):
        self.name = name
        self.contact_info = contact_info
        self.property_history = []

    def search_and_purchase_property(self, property):
        property.search_and_purchase_property(self)
        self.property_history.append(property)

    def view_property_history(self):
        print(f"Property purchase history for {self.name}:")
        for property in self.property_history:
            print(property.address)

