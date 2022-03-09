def withdrawal(self, amount):
    self.balance -= amount
    if self.balance < 0
        print("Insufficient funds.")
    return self

def display_account_info(self):
    print(f"Balance: {self.balance}")