from abc import ABC, abstractmethod

from .accounts import CashAccount, BonusAccount, TotalSpentAccount
from .citizen import Citizen


class PaymentTerminal(ABC):
    """Абстрактный класс платежного терминала"""

    def __init__(self, transaction_sum: int):
        self._sum = transaction_sum

    @abstractmethod
    def process_cash_operation(self, cash_account: CashAccount):
        ...

    @abstractmethod
    def process_bonus_operation(self, bonus_account: BonusAccount):
        ...

    @abstractmethod
    def process_total_spent_operation(self, total_spent_account: TotalSpentAccount):
        ...

    @abstractmethod
    def notify(self, citizen: Citizen):
        ...

    def dispatch_operation(self, citizen: Citizen):
        self.process_cash_operation(citizen.cash_account)
        self.process_bonus_operation(citizen.bonus_account)
        self.process_total_spent_operation(citizen.total_spent_account)
        self.notify(citizen)


class CafeTerminal(PaymentTerminal):
    """Платежный терминал в кафе"""

    def process_cash_operation(self, cash_account: CashAccount):
        cash_account.pay(self._sum)

    def process_bonus_operation(self, bonus_account: BonusAccount):
        bonus_account.accrue(self._sum * .1)

    def process_total_spent_operation(self, total_spent_account: TotalSpentAccount):
        total_spent_account.accrue(self._sum)

    def notify(self, citizen: Citizen):
        print(f'Добро пожаловать в кафе! Спасибо за покупку на {self._sum} рублей! Приятного аппетита!')


class CinemaTerminal(CafeTerminal):
    """Платежный терминал в кинотеатре"""

    def process_bonus_operation(self, bonus_account: BonusAccount):
        bonus_account.accrue(self._sum * .15)

    def notify(self, citizen: Citizen):
        print(f'Добро пожаловать в кинотеатр! Спасибо за покупку на {self._sum} рублей! Приятного просмотра!')


class UtilityServiceTerminal(CafeTerminal):
    """Платежный терминал в коммунальном сервисе"""

    def process_cash_operation(self, cash_account: CashAccount):
        super().process_cash_operation(cash_account)
        cash_account.write_off(self._sum * .1)

    def process_bonus_operation(self, bonus_account: BonusAccount):
        pass

    def notify(self, citizen: Citizen):
        print(f'Спасибо за добровольное пожертвование.')


class JobTerminal(PaymentTerminal):
    """Платежный терминал на работе"""

    def process_cash_operation(self, cash_account: CashAccount, citizen_name: str):
        cash_account.accrue(len(citizen_name) * 100)

    def process_bonus_operation(self, bonus_account: BonusAccount):
        pass

    def process_total_spent_operation(self, total_spent_account: TotalSpentAccount):
        pass

    def notify(self, citizen: Citizen):
        print(f'Поздравляем с зарплатой!')

    def dispatch_operation(self, citizen: Citizen, citizen_name: str):
        self.process_cash_operation(citizen.cash_account, citizen_name)
        self.notify(citizen)
