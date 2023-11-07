from abc import ABC, abstractmethod

# Abstract class for real estate operations
class Property(ABC):
    @abstractmethod
    def list_property(self, agent):
        pass

    @abstractmethod
    def search_and_purchase_property(self, client):
        pass

# Concrete classes for different types of properties
class ResidentialProperty(Property):
    def __init__(self, address, price, features):
        self.address = address
        self.price = price
        self.features = features

    def list_property(self, agent):
        print(f"{agent.name} listed a residential property at {self.address} for ${self.price}")

    def search_and_purchase_property(self, client):
        print(f"{client.name} purchased the residential property at {self.address} for ${self.price}")

class CommercialProperty(Property):
    def __init__(self, address, price, features):
        self.address = address
        self.price = price
        self.features = features

    def list_property(self, agent):
        print(f"{agent.name} listed a commercial property at {self.address} for ${self.price}")

    def search_and_purchase_property(self, client):
        print(f"{client.name} purchased the commercial property at {self.address} for ${self.price}")

