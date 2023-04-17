from accounts import ICashAccount, IBonusAccount, ITotalSpentAccount

class Citizen:

    def __init__(self,
        name: str,
        cash_account: ICashAccount,
        bonus_account: IBonusAccount,
        total_spent_account: ITotalSpentAccount
    ):
        self.name = name
        self.cash_account = cash_account
        self.bonus_account = bonus_account
        self.total_spent_account = total_spent_account
