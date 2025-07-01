import random, math, datetime, sys
class account:
    def __init__(self, holder_name, bal, acctype):
        self.name = holder_name
        self.bal = bal
        self.acctType = acctype
    def fun1(self, amount):
        self.bal = self.bal + amount
        print('New balance: ' + str(self.bal))
    def fun2(self, amount):
        if self.bal < amount:
            print("Insufficient funds!")
            return
        self.bal = self.bal - amount
        print('New balance: ' + str(self.bal))
class saving(account):
    def __init__(self, holder_name, bal, acctype, rate=0.03):
        super().__init__(holder_name, bal, acctype)
        self.interest_rate = rate
    def calculateinterest(self):
        interest = self.bal * self.interest_rate
        print("Interest: ", interest)
        return interest
class Current(account):
    def __init__(self, holder_name, bal, acctype):
        super().__init__(holder_name, bal, acctype)
    def withdraw(self, amount):
        if self.bal < 0:
            print("Overdraft not allowed!")
            return
        super().Withdraw(amount)
def Transaction_history():
    history = []
    for i in range(random.randint(5, 15)):
        history.append(f"Transaction {i+1} at {datetime.datetime.now()}")
    return history
acc1 = saving('Ali', 1000, 'savings')
acc1.fun1(500)
acc1.calculateinterest()
acc2 = Current('Ahmed', 2000, 'current')
acc2.fun2(300)
history = Transaction_history()
print(history)
