from BankingOperation import BankingOperation
from validate_decorators import validate_email, validate_non_empty_string

class Customer(BankingOperation):
    @validate_non_empty_string("name")
    @validate_email("contact_info")
    def __init__(self, name, contact_info):
        self.name = name
        self.contact_info = contact_info
        self.accounts = []

    def manage_account(self, account, initial_balance=0.0):
        account.balance = initial_balance
        self.accounts.append(account)

    def view_transaction_history(self, account):
        print(f"Transaction history for account {account.account_number} ({account.account_type}):")
    

    def transfer_funds(self, from_account, to_account, amount):
        if from_account in self.accounts and to_account in self.accounts:
            if from_account.balance >= amount:
                from_account.balance -= amount
                to_account.balance += amount
                print(f"Transfer of ${amount} from {from_account.account_number} to {to_account.account_number} completed.")
            else:
                print(f"Insufficient funds in account {from_account.account_number}.")
        else:
            print("Invalid account selection.")