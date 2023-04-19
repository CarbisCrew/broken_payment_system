from accounts.accounts import CashAccount, BonusAccount, TotalSpentAccount


class Citizen:

    def __init__(self, name: str,
                 cash_account: CashAccount, 
                 bonus_account: BonusAccount,
                 total_spent_account: TotalSpentAccount):
        
        self.name = name
        self.cash_account = cash_account
        self.bonus_account = bonus_account
        self.total_spent_account = total_spent_account

    def get_balance(self) -> dict:
        return {'Cash': self.cash_account.balance,
                'Bonus': self.bonus_account.balance,
                'Total_spent': self.total_spent_account.balance,
                }


