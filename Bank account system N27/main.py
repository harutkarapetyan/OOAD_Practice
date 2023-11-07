from Customer import Customer
from Account import IndividualAccount


if __name__ == "__main__":
    
    customer1 = Customer("Alice", "alice@example.com")

    individual_account1 = IndividualAccount("077076")
    individual_account2 = IndividualAccount("055056")

    customer1.manage_account(individual_account1, 900)
    customer1.manage_account(individual_account2, 500)

    customer1.view_transaction_history(individual_account1)
    customer1.view_transaction_history(individual_account2)

    customer1.transfer_funds(individual_account1, individual_account2, 300)

    customer1.view_transaction_history(individual_account1)
    customer1.view_transaction_history(individual_account2)

