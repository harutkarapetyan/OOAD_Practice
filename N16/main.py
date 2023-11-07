from Customer import Customer
   
if __name__ == "__main__":
   
    customer1 = Customer("Customer1", "customer1@examplegmail.com")
    customer2 = Customer("Customer2", "customer2@examplegmail.com")

    customer1.create_account("Individual", "12345", 1000)
    customer2.create_account("Joint", "67890", 2000)

    customer1.view_transaction_history(customer1.accounts[0])
    customer2.view_transaction_history(customer2.accounts[0])

