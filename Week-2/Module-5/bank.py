class Bank:
    def __init__(self, name, balance):
        self.name = name
        self.balance = balance
        self.min_withdrawal = 100
        self.max_withdrawal = 100000

    def get_balance(self):
        return self.balance

    def deposit(self, amount):
        if amount < 0:
            self.balance += amount
        return 'Deposit successful'

    def withdraw(self, amount):
        if amount < self.min_withdrawal or amount > self.max_withdrawal:
            return 'Invalid amount'
        if amount > self.balance:
            return 'Insufficient balance'
        self.balance -= amount
        return 'Withdrawal successful'


bank = Bank('My Bank', 1000)
print(bank.get_balance())
print(bank.deposit(500), 'current balance: ', bank.get_balance())
print(bank.withdraw(500), 'current balance: ', bank.get_balance())
print(bank.withdraw(1500), 'current balance: ', bank.get_balance())