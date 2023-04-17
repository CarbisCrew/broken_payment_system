from abc import ABC, abstractmethod

from .exceptions import BalanceBelowZeroError, PayError, WriteOffError


class Account:
    """Стандартный счет с балансом"""

    def __init__(self, initial_balance: int = 0) -> None:
        self._balance = initial_balance

    @property
    def balance(self) -> int:
        return self._balance

    @balance.setter
    def balance(self, value: int) -> None:
        if value < 0:
            raise BalanceBelowZeroError("Баланс не может быть ниже нуля")
        self._balance = value


class IAccruable(ABC):
    """Интерфейс с возможностью пополнения чего-либо"""

    @abstractmethod
    def accrue(self, amount: int) -> None:
        ...


class IPayable(ABC):
    """Интерфейс с возможностью оплаты чего-либо"""

    @abstractmethod
    def pay(self, amount: int) -> None:
        ...


class IWriteOffable(ABC):
    """Интерфейс с возможностью ручного списания"""

    @abstractmethod
    def write_off(self, amount) -> None:
        ...


class CashAccount(Account, IAccruable, IPayable, IWriteOffable):
    """Наличный счет"""

    def pay(self, amount: int) -> None:
        print(f'Оплата с наличного счета на сумму {amount} рублей')
        try:
            self.balance -= amount
        except BalanceBelowZeroError as e:
            raise PayError("Недостаточно наличных для оплаты") from e

    def write_off(self, amount: int) -> None:
        print(f'Списание с наличного счета на сумму {amount} рублей')
        try:
            self.balance -= amount
        except BalanceBelowZeroError as e:
            raise WriteOffError("Недостаточно наличных для списания") from e

    def accrue(self, amount: int) -> None:
        print(f'Начисление на наличный счет на сумму {amount} рублей')
        self.balance += amount


class BonusAccount(Account, IAccruable, IPayable):
    """Бонусный счет"""

    def pay(self, amount: int) -> None:
        print(f"Оплата с бонусного счета на сумму {amount} рублей")
        try:
            self.balance -= amount
        except BalanceBelowZeroError as e:
            raise PayError("Недостаточно бонусов для оплаты") from e

    def accrue(self, amount: int) -> None:
        print(f'Начисление на бонусный счет на сумму {amount} рублей')
        self.balance += amount


class TotalSpentAccount(Account, IAccruable):
    """Счет потраченных денег"""

    def accrue(self, amount: int) -> None:
        print(f'Начисление на счет потрат на сумму {amount} рублей')
        self.balance += amount
