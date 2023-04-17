from abc import ABC, abstractmethod
from accounts import BaseAccount
from typing import Iterable
from accounts import CashAccount,PaymentError
from citizen import Citizen

class BasePaymentTerminal():
    def __init__(self, transaction_sum: int = 0):
        if transaction_sum < 0:
            raise PaymentError('Сумма платежа не может быть отрицательной')
        self.__sum__ = transaction_sum
        

    @property
    def sum(self) -> int:
        return self.__sum__

    # @sum.setter
    # def sum(self,value):
    #     if value < 0:
    #         raise PaymentError('Сумма платежа не может быть отрицательной')
    #     self.__sum__ = value
   

class IProcess_cash_opertation(ABC):
    @abstractmethod
    def process_cash_operation(self, cash_account: BaseAccount):
        ...

class IProcess_bonus_operation(ABC):
    @abstractmethod
    def process_bonus_operation(self, cash_account: BaseAccount):
        ...

class IProcess_total_spent_operation(ABC):
    @abstractmethod
    def process_total_spent_operation(self, cash_account: BaseAccount):
        ...

class INotify(ABC):
    @abstractmethod
    def notify(self, citizen: Citizen):
        ...
class IDispatch_operation(ABC):
    @abstractmethod
    def dispatch_operation(self, citizen: Citizen):
        ...


# Платежный терминал в кафе
class CafeTerminal(BasePaymentTerminal,IProcess_bonus_operation,IDispatch_operation,INotify,IProcess_total_spent_operation,IProcess_cash_opertation):
    
    def process_cash_operation(self, cash_account: BaseAccount):
        cash_account.pay(self.sum)

    def process_bonus_operation(self, bonus_account: BaseAccount):
        bonus_account.accrue(self.sum * .1)

    def process_total_spent_operation(self, total_spent_account: BaseAccount):
        total_spent_account.accrue(self.sum)

    def notify(self, citizen: Citizen):
        print(f'Добро пожаловать в кафе! Спасибо за покупку на {self.sum} рублей! Приятного аппетита!')

    def dispatch_operation(self, citizen: Citizen,account:BaseAccount):
        self.process_cash_operation(account)
        if isinstance(account,CashAccount):
            self.process_bonus_operation(citizen.bonus_account)
        self.process_total_spent_operation(citizen.total_spent_account)
        self.notify(citizen)
# # Платежный терминал в кинотеатре
class CinemaTerminal(CafeTerminal):

    def process_bonus_operation(self, bonus_account: BaseAccount):
        bonus_account.accrue(self.sum * .15)

    def notify(self, citizen: Citizen):
        print(f'Добро пожаловать в кинотеатр! Спасибо за покупку на {self.sum} рублей! Приятного просмотра!')


# # Платежный терминал в комунальном сервисе
class UtilityServiceTerminal(BasePaymentTerminal,IDispatch_operation,INotify,IProcess_total_spent_operation,IProcess_cash_opertation):

    def process_cash_operation(self, cash_account: BaseAccount):
        cash_account.pay(self.sum) 
        cash_account.writeoff(self.sum * .1)

    def notify(self, citizen: Citizen):
        print(f'Спасибо за добровольное пожертвование.')

    def process_total_spent_operation(self, total_spent_account: BaseAccount):
        total_spent_account.accrue(self.sum * 1.1)

    def dispatch_operation(self, citizen: Citizen):
        self.process_cash_operation(citizen.cash_account)
        self.process_total_spent_operation(citizen.total_spent_account)
        self.notify(citizen)

# Палтежный терминал на работе
class JobTerminal(BasePaymentTerminal,IProcess_cash_opertation,INotify,IDispatch_operation):
    
    def process_cash_operation(self, cash_account, citizen_name: str):
        cash_account.accrue(len(citizen_name) * 100)

    def notify(self, citizen: Citizen):
        print(f'Поздравляем с зарплатой!')

    def dispatch_operation(self, citizen: Citizen, citizen_name: str):
        self.process_cash_operation(citizen.cash_account, citizen_name)
        self.notify(citizen)
        
