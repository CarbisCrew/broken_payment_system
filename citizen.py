from accounts import CashAccount, BonusAccount, TotalSpentAccount
from notify import Notify

class Citizen:

    def __init__(self, name: str, cash_account:CashAccount, bonus_account:BonusAccount, total_spent_account:TotalSpentAccount):
        self.name = name
        self.cash_account = cash_account
        self.bonus_account = bonus_account
        self.total_spent_account = total_spent_account

    @property
    def salary(self):
        return len(''.join(self.name.split(' ')))*100
    @property
    def cash_balance(self):
        return self.cash_account.balance
    @property
    def bonus_balance(self):
        return self.bonus_account.balance
    @property
    def total_balance(self):
        return self.total_spent_account.balance
    
    def get_balance(self):
        itogi = f"Наличный счет: {self.cash_balance}\n"
        itogi += f"Бонусный счет: {self.bonus_balance}\n"
        itogi += f"Счет потрат: {self.total_balance}\n"
        Notify(itogi).message_send()