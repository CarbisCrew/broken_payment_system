from abc import ABC, abstractmethod
from notify import Notify

class PaymentError(Exception):
    ...

class Account(ABC):
    def __init__(self, initial_balance: int = 0) -> None:
        self.__balance__ = initial_balance

    @property
    def balance(self) -> int:
        return self.__balance__
    
    def _notify(self, message: str):
        Notify(message).message_send()

class IPayAccount(ABC):
    @abstractmethod
    def pay(self, sum: int):
        pass

class IWriteoffAccount(ABC):
    @abstractmethod
    def writeoff(self, sum: int):
        pass

class IAccrueAccount(ABC):
    @abstractmethod
    def accrue(self, sun: int):
        pass

class CashAccount(Account, IPayAccount, IWriteoffAccount, IAccrueAccount):
    def pay(self, sum: int):
        self._notify(f'Оплата с наличного счета на сумму {sum} рублей')
        if self.__balance__ < sum:
            raise PaymentError('Недостаточно средств')
        self.__balance__-=sum

    def writeoff(self, sum:int):
        self._notify(f'Списание с наличного счета на сумму {sum} рублей')
        self.__balance__-=sum

    def accrue(self, sum: int):
        self._notify(f'Начисление на наличный счет на сумму {sum} рублей')
        self.__balance__+=sum

class BonusAccount(Account, IPayAccount, IAccrueAccount):

    def pay(self, sum: int):
        self._notify(f'Оплата с бонусного счета на сумму {sum} рублей')
        if self.__balance__ < sum:
            raise PaymentError('Недостаточно средств')
        self.__balance__-=sum

    def accrue(self, sum: int):
        self._notify(f'Начисление на бонусный счет на сумму {sum} рублей')
        self.__balance__+=sum

class TotalSpentAccount(Account, IAccrueAccount):

    def accrue(self, sum: int):
        self._notify(f'Начисление на счет потрат на сумму {sum} рублей')
        self.__balance__+=sum