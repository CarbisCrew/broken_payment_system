from abc import ABC, abstractmethod

from citizen import Citizen
from accounts.acc_interfaces import IBalance
from accounts.accounts import TotalSpentAccount, BonusAccount


class IProcessOperation:

    @abstractmethod
    def process_operation(self, billing_account: IBalance, sum: int):
        ...

    @abstractmethod
    def process_operation(self, billing_account: IBalance, sum: int):
        ...

    @abstractmethod
    def add_bonuses(self, billing_account: BonusAccount, sum: int):
        ...

    @abstractmethod
    def add_total(self, billing_account: TotalSpentAccount, sum: int):
        ...

class INotifier:

    @abstractmethod
    def notify(self, citizen: Citizen):
        ...

class PaymentTerminal(ABC):

    def dispatch_operation(self, citizen: Citizen, sum: int, use_bonus: bool = False):
        if use_bonus:
            self.process_operation(citizen.bonus_account, sum)
        else:
            self.process_operation(citizen.cash_account, sum)
            self.add_bonuses(citizen.bonus_account, sum)
            self.add_total(citizen.total_spent_account, sum)
        self.notify(citizen)
