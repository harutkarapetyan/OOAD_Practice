from Accaunt import IndividualAccount, JointAccount
from validate_decorators import validate_non_empty_string, validate_email

class Customer:
    @validate_email("contact_info")
    @validate_non_empty_string("name")
    def __init__(self, name, contact_info):
        self.name = name
        self.contact_info = contact_info
        self.accounts = []

    def create_account(self, account_type, account_number, initial_balance):
        if account_type == "Individual":
            account = IndividualAccount(account_number, initial_balance)
        elif account_type == "Joint":
            account = JointAccount(account_number, initial_balance)
        self.accounts.append(account)

    def view_transaction_history(self, account):
        print(f"Transaction history for Account {account.account_number} ({account.account_type}):")
        for transaction in account.transactions:
            print(f"- Type: {transaction.transaction_type}, Amount: {transaction.amount}")
