#Sample Code from Learning Platform
# class User:
#     def example_method(self):
#         self.account.deposit(100)		# we can call the BankAccount instance's methods
#     	print(self.account.balance)		# or access its attributes
class BankAccount:
    accounts = []
    def __init__(self, interest_rate, balance):
        self.interest_rate = interest_rate
        self.balance = balance
        BankAccount.accounts.append(self)

class User:
    def _init_(self, name):
        self.name = name
        self.account = {
            "checking" : BankAccount(.02, 1000),
            "savings" : BankAccount(.05, 3000)
        }

    def display_balance(self):
        print(f"User: {self.name}, Checking Balance: {self.account['checking'].display_account_info()}")
        print(f"User: {self.name}, Savings Balance: {self.account['savings'].display_account_info()}")
        return self

    def transfer_money(self, amount, user):
        self.amount -= amount
        user.amount += amount
        self.display_balance()
        user.display_balance()
        return self
    
#instance of user
michele = User("Michele Helm")

michele.account['checking'].deposit(100)
michele.display_balance()
