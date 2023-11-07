from abc import ABC, abstractmethod

class BankingOperation(ABC):
    @abstractmethod
    def manage_account(self):
        pass

    @abstractmethod
    def view_transaction_history(self):
        pass

    @abstractmethod
    def transfer_funds(self, from_account, to_account, amount):
        pass