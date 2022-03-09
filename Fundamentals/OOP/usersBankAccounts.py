#Sample Code from Learning Platform
# class User:
#     def example_method(self):
#         self.account.deposit(100)		# we can call the BankAccount instance's methods
#     	print(self.account.balance)		# or access its attributes

class User:
    def _init_(self, name):
        self.name = name
        self.account = 0

class other_User:
    def _init_(self, name):
        self.name = name
        self.account = 0

    def deposit_money(self, amount):
        self.account += amount
        return self
    
    def withdraw_money(self, amount):
        self.account -= amount
        return self
    
    def transfer_money(self, amount, other_User):
        self.account -= amount
        other_User.account += amount
        self.display_balance()
        other_User.display_balance()
        return self
    
    def display_balance(self):
        print(f"User: {self.name}, Balance: {self.account}")
        return self
    
michele = User("Michele Helm")

# guido.make_deposit(863659)




