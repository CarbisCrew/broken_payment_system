from .accounts import CashAccount, BonusAccount, TotalSpentAccount


class Citizen:
    def __init__(self, name: str,
                 cash_account: CashAccount,
                 bonus_account: BonusAccount,
                 total_spent_account: TotalSpentAccount):
        self._name = name
        self.cash_account = cash_account
        self.bonus_account = bonus_account
        self.total_spent_account = total_spent_account

    @property
    def name(self) -> str:
        return self._name
