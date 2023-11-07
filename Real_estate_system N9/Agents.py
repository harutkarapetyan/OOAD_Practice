from validate_decorators import validate_email, validate_non_empty_string

class Agent:
    @validate_non_empty_string("name")
    @validate_email("contact_info")
    def __init__(self, name, contact_info):
        self.name = name
        self.contact_info = contact_info
        self.property_listings = []

    def list_property(self, property):
        property.list_property(self)
        self.property_listings.append(property)

    def manage_clients(self, client):
        print(f"{self.name} is managing client information for {client.name}")
