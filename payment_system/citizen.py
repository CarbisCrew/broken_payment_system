from accounts import CashAccount, BonusAccount, TotalSpentAccount


class Citizen:
    def __init__(self, name):
        self.name = name
        self.cash_account = CashAccount()
        self.bonus_account = BonusAccount()
        self.total_spent_account = TotalSpentAccount()
