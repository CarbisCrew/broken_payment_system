from accounts import BaseAccount

class Citizen:

    def __init__(self,cash_account:BaseAccount,bonus_account:BaseAccount,total_spent_account:BaseAccount):
        self.cash_account = cash_account
        self.bonus_account = bonus_account
        self.total_spent_account = total_spent_account
