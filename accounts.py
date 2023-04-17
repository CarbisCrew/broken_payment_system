from typing import Iterable
from abc import ABC, abstractmethod

class PaymentError(Exception):
    ...


class IAccount(ABC):

    def __init__(self, initial_balance: int = 0) -> None:
        self.__balance__ = initial_balance

    @property
    def balance(self) -> int:
        return self.__balance__
    

class IPay(IAccount):
    
    @abstractmethod
    def pay(self, sum: int):
        ...



class IWriteoff(IAccount):
    
    @abstractmethod
    def writeoff(self, sum: int):
        ...


class IAccrue(IAccount):
    
    @abstractmethod
    def accrue(self, sum: int):
        ...
    
    # @abstractmethod
    # def apply_transaction(self, sum: int):



class ICashAccount(IPay, IWriteoff, IAccrue):
    ...


class IBonusAccount(IPay, IAccrue):
    ...


class ITotalSpentAccount(IAccrue):
    ...


# Наличный счет
class CashAccount(ICashAccount):
    
    def pay(self, sum: int):
        if self.balance < sum:
            raise PaymentError('Недостаточно средств')
        print(f'Оплата с наличного счета на сумму {sum} рублей')
        self.__balance__ -= sum
        
    def writeoff(self, sum: int):
        print(f'Списание с наличного счета на сумму {sum} рублей')
        self.__balance__ -= sum

    def accrue(self, sum: int):
        print(f'Начисление на наличный счет на сумму {sum} рублей')
        self.__balance__ += sum

       

# Бонусный счет
class BonusAccount(IBonusAccount):

    def pay(self, sum: int):
        if self.balance < sum:
            raise PaymentError('Недостаточно средств')
        print(f'Оплата с бонусного счета на сумму {sum} рублей')
        self.__balance__ -= sum

    def accrue(self, sum: int):
        print(f'Начисление на бонусный счет на сумму {sum} рублей')
        self.__balance__ += sum


# Счет потрат
class TotalSpentAccount(ITotalSpentAccount):

    def accrue(self, sum: int):
        print(f'Начисление на счет потрат на сумму {sum} рублей')
        self.__balance__ += sum
        