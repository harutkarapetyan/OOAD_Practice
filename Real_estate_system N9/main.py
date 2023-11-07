from Clients import Client
from Agents import Agent
from Properties import ResidentialProperty, CommercialProperty

if __name__ == "__main__":
    
    agent1 = Agent("Agent John", "agent.smith@example.com")
    agent2 = Agent("Agent Bob", "agent.johnson@example.com")

    client1 = Client("Alice", "alice@examplegmail.com")
    client2 = Client("Bibo", "bob@examplegmail.com")

    residential_property = ResidentialProperty("123 Main St.", 25000, "3 bedrooms, 2 bathrooms")
    commercial_property = CommercialProperty("456 Oak Ave.", 70000, "Office space, parking lot")

    agent1.list_property(residential_property)
    agent2.list_property(commercial_property)

    client1.search_and_purchase_property(residential_property)
    client2.search_and_purchase_property(commercial_property)

    client1.view_property_history()
    client2.view_property_history()

    agent1.manage_clients(client1)
    agent2.manage_clients(client2)





