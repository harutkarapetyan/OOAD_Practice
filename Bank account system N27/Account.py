
class Account:
    def __init__(self, account_number, account_type):
        self.account_number = account_number
        self.account_type = account_type
        self.balance = 0.0


class IndividualAccount(Account):
    def __init__(self, account_number):
        super().__init__(account_number, "Individual")

class BusinessAccount(Account):
    def __init__(self, account_number):
        super().__init__(account_number, "Business")
