class User:
    def __init__(self, name, balance):
        self.name = name
        self.balance = balance

    def make_withdrawal(self, amount):
        self.balance -= amount
        return self
    
    def make_deposit(self, amount):
        self.balance += amount
        return self
    
    def display_user_balance(self):
        print(self.balance)
        return self
    
    def transfer_money(self, other_user, amount):
        self.balance -= amount
        other_user.balance += amount
        return self

account1 = User("Ricky Bobby", 40000)
account2 = User("Joe Park", 999999)
account3 = User("Big Bertha", 500000)

account1.make_deposit(5000).make_deposit(2300).make_deposit(1060).make_withdrawal(900).display_user_balance()

account2.make_deposit(500).make_deposit(500).make_withdrawal(7000).make_withdrawal(2400).display_user_balance()

account3.make_deposit(1700).make_withdrawal(450).make_withdrawal(750).make_withdrawal(950).display_user_balance()

account1.transfer_money(account3, 20000).display_user_balance()
account3.display_user_balance()