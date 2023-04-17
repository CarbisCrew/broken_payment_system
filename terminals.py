from abc import ABC, abstractmethod
from citizen import Citizen
from notify import Notify

class PaymentTerminal(ABC):
    def __init__(self, citzen: Citizen):
        self.__citzen__ = citzen
    
    def _notify(self, message: str):
        notify = Notify(message)
        notify.sms_send()

class CashOperation(PaymentTerminal):
    @abstractmethod
    def process_cash_operation(self, sum: int):
        pass

class BonusOperation(PaymentTerminal):
    @abstractmethod
    def process_bonus_operation(self, sum: int):
        pass

# Платежный терминал в кафе
class CafeTerminal(CashOperation, BonusOperation):
    def process_cash_operation(self, sum: int):
        try:
            self.__citzen__.cash_account.pay(sum)
            self.__citzen__.bonus_account.accrue(sum*.1)
            self.__citzen__.total_spent_account.accrue(sum)
            self._notify(f'Добро пожаловать в кафе! Спасибо за покупку на {sum} рублей! Приятного аппетита!')
        except Exception as e:
            print(e)

    def process_bonus_operation(self, sum: int):
        try:
            self.__citzen__.bonus_account.pay(sum)
            self._notify(f'Добро пожаловать в кафе! Спасибо за покупку на {sum} рублей! Приятного аппетита!')
        except Exception as e:
            print(e)

# Платежный терминал в кинотеатре
class CinemaTerminal(CashOperation, BonusOperation):
    def process_cash_operation(self, sum: int):
        try:
            self.__citzen__.cash_account.pay(sum)
            self.__citzen__.bonus_account.accrue(sum*.15)
            self.__citzen__.total_spent_account.accrue(sum)
            self._notify(f'Добро пожаловать в кинотеатр! Спасибо за покупку на {sum} рублей! Приятного просмотра!')
        except Exception as e:
            print(e)

    def process_bonus_operation(self, sum: int):
        try:
            self.__citzen__.bonus_account.pay(sum)
            self._notify(f'Добро пожаловать в кинотеатр! Спасибо за покупку на {sum} рублей! Приятного просмотра!')
        except Exception as e:
            print(e)

# Платежный терминал в комунальном сервисе
class UtilityServiceTerminal(CashOperation):
    def process_cash_operation(self, sum: int):
        try:
            self.__citzen__.cash_account.pay(sum)
            self.__citzen__.total_spent_account.accrue(sum)
            self._notify(f'Оплата комунальных услуг на сумму {sum} рублей!')
            self.__citzen__.cash_account.writeoff(sum*.1)
            self.__citzen__.total_spent_account.accrue(sum*.1)
            self._notify('Спасибо за пожертвование')
        except Exception as e:
            print(e)

# Палтежный терминал на работе
class JobTerminal(CashOperation):
    def process_cash_operation(self, sum: int):
        self.__citzen__.cash_account.accrue(sum)
        self._notify(f'Начисление зарплаты')
