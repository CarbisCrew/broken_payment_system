from abc import ABC, abstractmethod

from .citizen import Citizen


class PaymentTerminal(ABC):
    """Абстрактный класс платежного терминала"""

    def __init__(self, transaction_sum: int) -> None:
        self._sum = transaction_sum

    @abstractmethod
    def _notify(self) -> None:
        ...


class PayableWithCash(ABC):
    """Интерфейс с возможностью оплаты наличностью"""

    @abstractmethod
    def process_cash_operation(self, citizen: Citizen) -> None:
        ...


class PayableWithBonuses(ABC):
    """Интерфейс с возможностью оплаты бонусами"""

    @abstractmethod
    def process_bonus_operation(self, citizen: Citizen) -> None:
        ...


class CafeTerminal(PaymentTerminal, PayableWithCash, PayableWithBonuses):
    """Платежный терминал в кафе"""

    def process_cash_operation(self, citizen: Citizen) -> None:
        citizen.cash_account.pay(self._sum)
        citizen.bonus_account.accrue(int(self._sum * .1))
        citizen.total_spent_account.accrue(self._sum)
        self._notify()

    def process_bonus_operation(self, citizen: Citizen) -> None:
        citizen.bonus_account.pay(self._sum)
        self._notify()

    def _notify(self) -> None:
        print(f'Добро пожаловать в кафе! Спасибо за покупку на {self._sum} рублей! Приятного аппетита!')


class CinemaTerminal(PaymentTerminal, PayableWithCash, PayableWithBonuses):
    """Платежный терминал в кинотеатре"""

    def process_cash_operation(self, citizen: Citizen) -> None:
        citizen.cash_account.pay(self._sum)
        citizen.bonus_account.accrue(int(self._sum * .15))
        citizen.total_spent_account.accrue(self._sum)
        self._notify()

    def process_bonus_operation(self, citizen: Citizen) -> None:
        citizen.bonus_account.pay(self._sum)
        self._notify()

    def _notify(self) -> None:
        print(f'Добро пожаловать в кинотеатр! Спасибо за покупку на {self._sum} рублей! Приятного просмотра!')


class UtilityServiceTerminal(PaymentTerminal, PayableWithCash):
    """Платежный терминал в коммунальном сервисе"""

    def process_cash_operation(self, citizen: Citizen) -> None:
        citizen.cash_account.pay(self._sum)
        citizen.total_spent_account.accrue(self._sum)
        citizen.cash_account.write_off(int(self._sum * .1))
        self._notify()

    def _notify(self) -> None:
        print(f'Спасибо за добровольное пожертвование.')


class JobTerminal(PaymentTerminal, PayableWithCash):
    """Платежный терминал на работе"""

    def __init__(self) -> None:
        ...

    def process_cash_operation(self, citizen: Citizen) -> None:
        citizen.cash_account.accrue(len(citizen.name) * 100)
        self._notify()

    def _notify(self) -> None:
        print("Поздравляем с зарплатой!")
