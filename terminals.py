from abc import ABC, abstractmethod
from accounts import PaymentError
from citizen import Citizen

# базовый класс терминала
class PaymentTerminal(ABC):
    def __init__(self, transaction_sum: int):
        self.__sum__ = transaction_sum

    @abstractmethod
    def notify(self):
        ...


# класс работы с наличкой
class CashPayment(PaymentTerminal):
    @abstractmethod
    def process_cash_operation(self, citizen: Citizen):
        ...

# класс работы с бонусами  
class BonusPayment(PaymentTerminal):
    @abstractmethod
    def process_bonus_operation(self, citizen: Citizen):
        ...

# оплата бонусами
class PaymentTerminalWithBonus(BonusPayment):
    def process_bonus_operation(self, citizen: Citizen):
        try:
            citizen.bonus_account.decrease_balance(self.__sum__)
            self.notify()
        except PaymentError as e:
            print(f"{e}. Воспользуйтесь другим способом оплаты.")

# Платежный терминал на работе
class JobTerminal(CashPayment):    
    def process_cash_operation(self, citizen: Citizen, citizen_name: str):
        citizen.cash_account.increase_balance((len(citizen_name)-citizen_name.count(" ")) * 100)
        self.notify()

    def notify(self):
        print(f'Поздравляем с зарплатой!')

# Платежный терминал в кафе
class CafeTerminal(PaymentTerminalWithBonus, CashPayment):
    def process_cash_operation(self, citizen: Citizen):
        citizen.cash_account.decrease_balance(self.__sum__)
        citizen.bonus_account.increase_balance(self.__sum__ * .1)
        citizen.total_spent_account.increase_balance(self.__sum__)
        self.notify()
    
    def notify(self):
        print(f'Добро пожаловать в кафе! Спасибо за покупку бонусами на {self.__sum__} рублей! Приятного аппетита!')

# Платежный терминал в кинотеатре
class CinemaTerminal(PaymentTerminalWithBonus, CashPayment):
    def process_cash_operation(self, citizen: Citizen):
        citizen.cash_account.decrease_balance(self.__sum__)
        citizen.bonus_account.increase_balance(self.__sum__ * .15)
        citizen.total_spent_account.increase_balance(self.__sum__)
        self.notify()

    def notify(self):
        print(f'Добро пожаловать в кинотеатр! Спасибо за покупку на {self.__sum__} рублей! Приятного просмотра!')


# Платежный терминал в комунальном сервисе
class UtilityServiceTerminal(CashPayment):

    def process_cash_operation(self, citizen: Citizen):
        citizen.cash_account.decrease_balance(self.__sum__)
        citizen.cash_account.decrease_balance(self.__sum__ * .1)
        citizen.total_spent_account.increase_balance(self.__sum__)
        self.notify()

    def notify(self):
        print(f'Спасибо за добровольное пожертвование.')
