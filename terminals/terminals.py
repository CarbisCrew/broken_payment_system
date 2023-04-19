from typing import Iterable

from citizen import Citizen
from accounts.acc_interfaces import IBalance
from .term_interfaces import PaymentTerminal, IProcessOperation, INotifier
from accounts.accounts import CashAccount, BonusAccount, TotalSpentAccount


# Платежный терминал в кафе
class CafeTerminal(PaymentTerminal, IProcessOperation, INotifier):
    
    def __init__(self) -> None:
        _sum = None

    def process_operation(self, billing_account: IBalance, sum: int):
        self._sum = sum
        billing_account.pay(sum)


    def add_bonuses(self, billing_account: BonusAccount, sum: int):
        billing_account.accrue(sum * .1)

    def notify(self, citizen: Citizen):
        print(f'Добро пожаловать в кафе! Спасибо за покупку на {self._sum} рублей! Приятного аппетита!')


# Платежный терминал в кинотеатре
class CinemaTerminal(PaymentTerminal, IProcessOperation, INotifier):

    def __init__(self) -> None:
        _sum = None

    def process_operation(self, billing_account: IBalance, sum: int):
        self._sum = sum
        billing_account.pay(sum)

    def add_bonuses(self, billing_account: BonusAccount, sum: int):
        billing_account.accrue(sum * .15)

    def notify(self, citizen: Citizen):
        print(f'Добро пожаловать в кинотеатр! Спасибо за покупку на {self._sum} рублей! Приятного просмотра!')


# Платежный терминал в комунальном сервисе
class UtilityServiceTerminal(PaymentTerminal, IProcessOperation, INotifier):

    def process_operation(self, billing_account: CashAccount, sum: int):
        billing_account.pay(sum)
        billing_account.write_off(sum * .1)
        
    def add_total(self, billing_account: TotalSpentAccount, sum: int):
        billing_account.accrue(sum)

    def notify(self, citizen: Citizen):
        print(f'Спасибо за добровольное пожертвование, {citizen.name}.')


# Палтежный терминал на работе
class JobTerminal(PaymentTerminal, IProcessOperation, INotifier):
    
    def process_operation(self, billing_account: CashAccount, sum: int):
        billing_account.accrue(sum)

    def notify(self, citizen: Citizen):
        print(f'Поздравляем с зарплатой, {citizen.name}!')
