class User:
    def __init__(self, name):
        self.name = name
        self.account_balance = 0
    
    def make_deposit(self, amount):
        self.account_balance += amount

    def make_withdrawal(self, amount):
        self.account_balance -= amount

    def display_balance(self):
        self.account_balance -= amount

# guido.make_deposit(123456)
#guido.make_withdrawal(654321)
#guido.display_user_balance()
# ^^ practice

michele = User("Michele Helm")
chloe = User("Chloe A.")

michele.transfer_money(1000, chloe)
michele.make_deposit(1200).make_deposit(800).make_withdrawal(2000).display_user_balance()
    

