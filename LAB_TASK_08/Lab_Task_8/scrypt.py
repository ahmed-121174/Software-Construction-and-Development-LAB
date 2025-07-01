"""Banking system simulation with account types and transaction history."""

import random
import datetime


class Account:
    """Base account class for common account operations."""

    def __init__(self, holder_name, bal, acctype):
        self.name = holder_name
        self.bal = bal
        self.acct_type = acctype

    def deposit(self, amount):
        """Deposits amount into account balance."""
        self.bal += amount
        print("New balance: " + str(self.bal))

    def withdraw(self, amount):
        """Withdraws amount from account balance if sufficient funds."""
        if self.bal < amount:
            print("Insufficient funds!")
            return
        self.bal -= amount
        print("New balance: " + str(self.bal))


class SavingAccount(Account):
    """Savings account with interest calculation."""

    def __init__(self, holder_name, bal, acctype, rate=0.03):
        super().__init__(holder_name, bal, acctype)
        self.interest_rate = rate

    def calculate_interest(self):
        """Calculates interest based on current balance and interest rate."""
        interest = self.bal * self.interest_rate
        print("Interest: ", interest)
        return interest


class CurrentAccount(Account):
    """Current account that disallows overdraft."""

    def withdraw(self, amount):
        """Withdraws from balance if no overdraft is present."""
        if self.bal < 0:
            print("Overdraft not allowed!")
            return
        super().withdraw(amount)


def generate_transaction_history():
    """Generates a list of random transaction timestamps."""
    transactions = []
    for i in range(random.randint(5, 15)):
        transactions.append(f"Transaction {i+1} at {datetime.datetime.now()}")
    return transactions


# Creating account instances and demonstrating functionality
acc1 = SavingAccount("Ali", 1000, "savings")
acc1.deposit(500)
acc1.calculate_interest()

acc2 = CurrentAccount("Ahmed", 2000, "current")
acc2.withdraw(300)

transaction_history = generate_transaction_history()
print(transaction_history)
