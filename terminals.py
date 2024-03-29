from abc import ABC, abstractmethod
from accounts import IAccount
from typing import Iterable
from citizen import Citizen

class PaymentTerminal(ABC):
    def __init__(self, transaction_sum: int):
        self.__sum__ = transaction_sum

    @abstractmethod
    def process_cash_operation(self, cash_account: IAccount):
        ...

    @abstractmethod
    def process_bonus_operation(self, bonus_account: IAccount):
        ...

    @abstractmethod
    def process_total_spent_operation(self, total_spent_account: IAccount):
        ...

    @abstractmethod
    def notify(self, citizen: Citizen):
        ...

    def dispatch_operation(self, citizen: Citizen):
        self.process_cash_operation(citizen.cash_account)
        self.process_bonus_operation(citizen.bonus_account)
        self.process_total_spent_operation(citizen.total_spent_account)
        self.notify(citizen)


# Платежный терминал в кафе
class CafeTerminal(PaymentTerminal):
    
    def process_cash_operation(self, cash_account: IAccount):
        cash_account.pay(self.__sum__)

    def process_bonus_operation(self, bonus_account: IAccount):
        bonus_account.accrue(self.__sum__ * .1)

    def process_total_spent_operation(self, total_spent_account: IAccount):
        total_spent_account.accrue(self.__sum__)

    def notify(self, citizen: Citizen):
        print(f'Добро пожаловать в кафе! Спасибо за покупку на {self.__sum__} рублей! Приятного аппетита!')


# Платежный терминал в кинотеатре
class CinemaTerminal(CafeTerminal):

    def process_bonus_operation(self, bonus_account: IAccount):
        bonus_account.accrue(self.__sum__ * .15)

    def notify(self, citizen: Citizen):
        print(f'Добро пожаловать в кинотеатр! Спасибо за покупку на {self.__sum__} рублей! Приятного просмотра!')


# Платежный терминал в комунальном сервисе
class UtilityServiceTerminal(CafeTerminal):

    def process_cash_operation(self, cash_account: IAccount):
        super().process_cash_operation(cash_account)
        cash_account.writeoff(self.__sum__ * .1)

    def process_bonus_operation(self, bonus_account: IAccount):
        pass

    def notify(self, citizen: Citizen):
        print(f'Спасибо за добровольное пожертвование.')


# Палтежный терминал на работе
class JobTerminal(PaymentTerminal):
    
    def process_cash_operation(self, cash_account: IAccount, citizen_name: str):
        cash_account.accrue(len(citizen_name) * 100)

    def process_bonus_operation(self, bonus_account: IAccount):
        pass

    def process_total_spent_operation(self, total_spent_account: IAccount):
        pass

    def notify(self, citizen: Citizen):
        print(f'Поздравляем с зарплатой!')

    def dispatch_operation(self, citizen: Citizen, citizen_name: str):
        self.process_cash_operation(citizen.cash_account, citizen_name)
        self.notify(citizen)
        
