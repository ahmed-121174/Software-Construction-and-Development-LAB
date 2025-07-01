"""
This script implements a basic banking system with different types of accounts and transactions.
"""

import datetime
import random


class Account:
    """
    This class represents a general bank account
    """

    def __init__(self, holder_name, bal, acc_type):
        """
        :param holder_name: str
        :param bal: int/float
        :param acc_type: str
        """
        self.name = holder_name
        self.bal = bal
        self.acc_type = acc_type

    def deposit(self, amount):
        """
        The function to deposit an amount
        :param amount: int/float
        """
        self.bal += amount
        print(f"New balance: {self.bal}")

    def withdraw(self, amount):
        """
        The function to withdraw an amount
        :param amount: int/float
        """
        if self.bal < amount:
            print("Insufficient funds!")
        else:
            self.bal -= amount
            print(f"New balance: {self.bal}")


class Saving(Account):
    """
    This class represents a saving account that inherits from the general bank account
    """

    def __init__(self, holder_name, bal, acc_type, rate=0.03):
        """
        :param holder_name: str
        :param bal: int/float
        :param acc_type: str
        :param rate: float
        """
        super().__init__(holder_name, bal, acc_type)
        self.interest_rate = rate

    def calculate_interest(self):
        """
        The function to calculate the interest
        """
        interest = self.bal * self.interest_rate
        print(f"Interest: {interest}")
        return interest


class Current(Account):
    """
    This class represents a current account that inherits from the general bank account
    """

    def withdraw(self, amount):
        """
        The function to withdraw an amount with additional check for overdraft
        :param amount: int/float
        """
        if self.bal < amount:
            print("Overdraft not allowed!")
        else:
            super().withdraw(amount)


def generate_transaction_history():
    """
    The function to generate a list of random transactions
    """
    trans_history = []
    for i in range(random.randint(5, 15)):
        trans_history.append(f"Transaction {i + 1} at {datetime.datetime.now()}")
    return trans_history


def main():
    """
    The main function to execute the banking operations
    """
    acc1 = Saving("Ali", 1000, "savings")
    acc1.deposit(500)
    acc1.calculate_interest()
    acc2 = Current("Ahmed", 2000, "current")
    acc2.withdraw(300)
    transaction_history = generate_transaction_history()
    print(transaction_history)


if __name__ == "__main__":
    main()
