from abc import ABC, abstractmethod

class PaymentError(Exception):
    ...

class IAccount(ABC):

    def __init__(self, initial_balance: int = 0) -> None:
        self.__balance__ = initial_balance

    @property
    def balance(self) -> int:
        return self.__balance__


class DecreaseBalance(IAccount):
    @abstractmethod
    def decrease_balance(self, sum: int):
        ...

class IncreaseBalance(IAccount):
    @abstractmethod
    def increase_balance(self, num:int):
        ...

# Наличный счет
class CashAccount(DecreaseBalance, IncreaseBalance):

    def decrease_balance(self, sum: int):
        if self.balance < sum:
            raise PaymentError('Недостаточно средств')
        print(f'Оплата или списание с наличного счета на сумму {sum} рублей')
        self.__balance__ -= sum

    def increase_balance(self, sum: int):
        print(f'Начисление на наличный счет на сумму {sum} рублей')
        self.__balance__ += sum


# Бонусный счет
class BonusAccount(DecreaseBalance, IncreaseBalance):

    def decrease_balance(self, sum: int):
        if self.balance < sum:
            raise PaymentError('Недостаточно средств')
        print(f'Оплата или списание с бонусного счета на сумму {sum} рублей')
        self.__balance__ -= sum

    def increase_balance(self, sum: int):
        print(f'Начисление на бонусный счет на сумму {sum} рублей')
        self.__balance__ += sum


class TotalSpentAccount(IncreaseBalance):

    def increase_balance(self, sum: int):
        print(f'Начисление на счет потрат на сумму {sum} рублей')
        self.__balance__ += sum