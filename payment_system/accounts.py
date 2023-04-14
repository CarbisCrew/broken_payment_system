from abc import ABC, abstractmethod

from .exceptions import PaymentError, BalanceBelowZeroError, PayError, WriteOffError


class AccountBalance:
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


class CashAccount(AccountBalance, IAccruable, IPayable, IWriteOffable):
    """Наличный счет"""

    def pay(self, amount: int):
        print(f'Оплата с наличного счета на сумму {amount} рублей')
        try:
            self.balance -= amount
        except BalanceBelowZeroError as e:
            raise PayError("Недостаточно средств для оплаты") from e

    def write_off(self, amount: int):
        print(f'Списание с наличного счета на сумму {amount} рублей')
        try:
            self.balance -= amount
        except BalanceBelowZeroError as e:
            raise WriteOffError("Недостаточно средств для списания") from e

    def accrue(self, amount: int):
        print(f'Начисление на наличный счет на сумму {amount} рублей')
        self.balance += amount


class BonusAccount(AccountBalance, IAccruable, IPayable):
    """Бонусный счет"""

    def pay(self, amount: int):
        print(f"Оплата с бонусного счета на сумму {amount} рублей")
        try:
            self.balance -= amount
        except BalanceBelowZeroError as e:
            raise PayError("Недостаточно средств для оплаты") from e

    def accrue(self, amount: int):
        print(f'Начисление на бонусный счет на сумму {amount} рублей')
        self.balance += amount


class TotalSpentAccount(AccountBalance, IAccruable):
    """Счет потраченных денег"""

    def accrue(self, amount: int):
        print(f'Начисление на счет потрат на сумму {amount} рублей')
        self.balance += amount
