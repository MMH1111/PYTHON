# Create a BankAccount class with the attributes interest rate and balance
class BankAccount:
    accounts = []
    def __init__(self, interest_rate, balance):
        self.interest_rate = interest_rate
        self.balance = balance
        BankAccount.accounts.append(self)

# Add a deposit method to the BankAccount class
    def deposit(self, amount):
        self.balance += amount
        return self

# Add a withdraw method to the BankAccount class
    def withdraw(self, amount):
        if (self.balance - amount) >= 0:
            self.balance -= amount
        else:
            print("Insufficient funds. Charging a $5 fee.")
            self.balance -= 5
        return self

# Add a display_account_info method to the BankAccount class
    def display_account_info(self):
        print(f"Balance: {self.balance}")
        return self

# Add a yield_interest method to the BankAccount class
    def yield_interest(self):
        if self.balance > 0:
            self.balance += (self.balance * self.interest_rate)
        return self

# NINJA BONUS: use a classmethod to print all instances of a Bank Account's info
@classmethod
def print_all_accounts(cls):
    for account in cls.accounts:
        account.display_account_info()

# Create 2 accounts
checking = BankAccount(.02, 5000)
savings = BankAccount(.05, 1000)

# To the first account, make 3 deposits and 1 withdrawal, 
# then yield interest and display the account's info all in one line of code (i.e. chaining)
checking.deposit(1200).deposit(800).deposit(1000).withdraw(2000).yield_interest().display_account_info()

# To the second account, make 2 deposits and 4 withdrawals, 
# then yield interest and display the account's info all in one line of code (i.e. chaining)
savings.deposit(1200).deposit(800).withdraw(100).withdraw(150).withdraw(200).withdraw(50).yield_interest().display_account_info()

BankAccount.display_account_info

