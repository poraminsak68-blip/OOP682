class BankAccount:
    def __init__(self, balance):
        self.balance = balance

    def __sub__(self, other):
        if isinstance(other, BankAccount):
            new_balance = self.balance - other.balance
            return BankAccount(new_balance)
        return NotImplemented

    def __add__(self, other):
        if isinstance(other, BankAccount):
            new_balance = self.balance + other.balance
            return BankAccount(new_balance)
        return NotImplemented

    def __str__(self):
        return f"BankAccount: {self.balance:,.2f}"
