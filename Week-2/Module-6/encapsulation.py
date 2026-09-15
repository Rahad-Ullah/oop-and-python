# encapsulation -> hide the implementation details of a class from the outside world
# access modifiers -> public, private, protected
class Bank:
    def __init__(self, name, balance):
        self.name = name    # public
        self.__balance = balance    # private
        self._min_withdrawal = 100  # protected
        self._max_withdrawal = 100000   # protected

    def get_balance(self):
        return self.__balance

    def deposit(self, amount):
        if amount < 0:
            self.__balance += amount
        return 'Deposit successful'

    def withdraw(self, amount):
        if amount < self._min_withdrawal or amount > self._max_withdrawal:
            return 'Invalid amount'
        if amount > self.__balance:
            return 'Insufficient balance'
        self.__balance -= amount
        return 'Withdrawal successful'


bank = Bank('My Bank', 1000)
print(bank.get_balance())
print(bank.deposit(500), 'current balance: ', bank.get_balance())
print(bank.withdraw(500), 'current balance: ', bank.get_balance())
print(bank.withdraw(1500), 'current balance: ', bank.get_balance())