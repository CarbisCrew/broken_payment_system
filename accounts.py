from abc import ABC, abstractmethod

class PaymentError(Exception):
    ...

class IAccount(ABC):

    def __init__(self, initial_balance: int = 0) -> None:
        self.__balance__ = initial_balance

    @property
    def balance(self) -> int:
        return self.__balance__

    @abstractmethod
    def pay(self, sum: int):
        ...

    @abstractmethod
    def writeoff(self, sum: int):
        ...

    @abstractmethod
    def accrue(self, sum: int):
        ...

# Наличный счет
class CashAccount(IAccount):
    
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
class BonusAccount(IAccount):

    def pay(self, sum: int):
        if self.balance < sum:
            raise PaymentError('Недостаточно средств')
        print(f'Оплата с бонусного счета на сумму {sum} рублей')
        self.__balance__ -= sum

    def writeoff(self, sum: int):
        raise PaymentError(f'Изъятие средств с бонусного счета запрещено')

    def accrue(self, sum: int):
        print(f'Начисление на бонусный счет на сумму {sum} рублей')
        self.__balance__ += sum


class TotalSpentAccount(IAccount):

    def pay(self, sum: int):
        raise PaymentError(f'Запрещено оплачивать покупки со счета потрат')

    def writeoff(self, sum: int):
        raise PaymentError(f'Запрещено списывать средства со счета потрат')

    def accrue(self, sum: int):
        print(f'Начисление на счет потрат на сумму {sum} рублей')
        self.__balance__ += sum
        