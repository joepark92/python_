class User:
    def __init__(self, name, balance):
        self.name = name
        self.balance = balance

    def make_withdrawal(self, amount):
        self.balance -= amount
    
    def make_deposit(self, amount):
        self.balance += amount
    
    def display_user_balance(self):
        print(self.balance)
    
    def transfer_money(self, other_user, amount):
        self.balance -= amount
        other_user.balance += amount

account1 = User("Ricky Bobby", 40000)
account2 = User("Joe Park", 999999)
account3 = User("Big Bertha", 500000)

account1.make_deposit(5000)
account1.make_deposit(2300)
account1.make_deposit(1060)
account1.make_withdrawal(900)
account1.display_user_balance()

account2.make_deposit(500)
account2.make_deposit(500)
account2.make_withdrawal(7000)
account2.make_withdrawal(2400)
account2.display_user_balance()

account3.make_deposit(1700)
account3.make_withdrawal(450)
account3.make_withdrawal(750)
account3.make_withdrawal(950)
account3.display_user_balance()

account1.transfer_money(account3, 20000)
account1.display_user_balance()
account3.display_user_balance()