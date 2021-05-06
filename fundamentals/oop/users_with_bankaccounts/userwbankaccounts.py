class BankAccount:
    bank_name = "Bank of Joe"
    all_accounts = []
    def __init__(self, name, int_rate = 0.2, balance = 0):
        self.name = name
        self.int_rate = int_rate
        self.balance = balance
        BankAccount.all_accounts.append(self)

    def deposit(self, amount):
        self.balance += amount
        return self

    def withdraw(self, amount):
        if BankAccount.can_withdraw(self.balance, amount):
            self.balance -= amount
        else:
            print("Insufficient funds.")
        return self

    def display_account_info(self):
        print(f"Your Balance: ${self.balance}")
        return self

    def yield_interest(self):
        self.balance += (self.balance * self.int_rate)
        return self

    @classmethod
    def change_bank_name(cls, name):
        cls.bank_name = name
        return cls

    @classmethod
    def all_balances(cls):
        for total in cls.all_accounts:
            total.display_account_info()

    @staticmethod
    def can_withdraw(balance, amount):
        if (balance - amount) < 0:
            return False
        else:
            return True

class User:
    def __init__(self, name, email):
        self.name = name
        self.email = email
        self.account = BankAccount(name='', int_rate = 0.05, balance = 0)

    def withdraw(self, amount):
        self.account.withdraw(amount)
        return self
    
    def deposit(self, amount):
        self.account.deposit(amount)
        return self
    
    def display_user_balance(self):
        print(f"User: {self.name}")
        self.account.display_account_info()
        return self
    
    def transfer_money(self, other_user, amount):
        self.balance -= amount
        other_user.balance += amount

joe = User("Joe", "joe@gmail.com")
bobby = User("Bobby", "bobby@gmail.com")

joe.deposit(2000).deposit(600).deposit(750).withdraw(1500).account.yield_interest()
joe.display_user_balance()
bobby.deposit(21000).deposit(875).withdraw(1300).withdraw(1500).withdraw(1200).withdraw(1700).account.yield_interest()
bobby.display_user_balance()