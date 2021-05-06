class BankAccount:
    bank_name = "Bank of Joe"
    all_accounts = []
    def __init__(self, int_rate = 0.2, balance = 0): 
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

account1 = BankAccount(0.1, 50000)
account2 = BankAccount(0.15, 75000)

account1.deposit(500).deposit(600).deposit(750).withdraw(1500).yield_interest().display_account_info()
account2.deposit(1000).deposit(875).withdraw(1300).withdraw(1500).withdraw(1200).withdraw(1700).yield_interest().display_account_info()

BankAccount.all_balances()