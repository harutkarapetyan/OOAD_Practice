from abc import ABC, abstractmethod
from Transaction import Transaction

# Abstract class for banking operations
class BankingOperation(ABC):
    @abstractmethod
    def deposit(self, amount):
        pass

    @abstractmethod
    def withdraw(self, amount):
        pass

    @abstractmethod
    def transfer(self, recipient, amount):
        pass

# Concrete classes for different types of accounts
class IndividualAccount(BankingOperation):
    def __init__(self, account_number, balance):
        self.account_number = account_number
        self.balance = balance
        self.account_type = "Individual"
        self.transactions = []

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            self.transactions.append(Transaction(self, amount, "Deposit"))

    def withdraw(self, amount):
        if amount > 0 and amount <= self.balance:
            self.balance -= amount
            self.transactions.append(Transaction(self, amount, "Withdrawal"))

    def transfer(self, recipient, amount):
        if amount > 0 and amount <= self.balance:
            self.balance -= amount
            self.transactions.append(Transaction(self, amount, "Transfer"))
            recipient.deposit(amount)

class JointAccount(BankingOperation):
    def __init__(self, account_number, balance):
        self.account_number = account_number
        self.balance = balance
        self.account_type = "Joint"
        self.transactions = []

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            self.transactions.append(Transaction(self, amount, "Deposit"))

    def withdraw(self, amount):
        if amount > 0 and amount <= self.balance:
            self.balance -= amount
            self.transactions.append(Transaction(self, amount, "Withdrawal"))

    def transfer(self, recipient, amount):
        if amount > 0 and amount <= self.balance:
            self.balance -= amount
            self.transactions.append(Transaction(self, amount, "Transfer"))
            recipient.deposit(amount)