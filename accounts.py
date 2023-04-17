from abc import ABC, abstractmethod

class PaymentError(Exception):
    ...

class BaseAccount():

    def __init__(self, initial_balance: int = 0) -> None:
        self.__balance__ = initial_balance

    @property
    def balance(self) -> int:
        return self.__balance__

    @balance.setter
    def balance(self,value):
        if value < 0:
            raise PaymentError('Баланс не может быть отрицательным')
        self.__balance__ = value
    
class IPayment(ABC):

    @abstractmethod
    def pay(self, sum: int):
        ...
class IWriteoff(ABC):
    
    @abstractmethod
    def writeoff(self, sum: int):
        ...
class IAccumulation(ABC): #??? 
    
    @abstractmethod
    def accrue(self, sum: int):
        ...

# Наличный счет
class CashAccount(BaseAccount,IPayment,IWriteoff,IAccumulation):
    
    def pay(self, sum: int):
        if self.balance < sum:
            raise PaymentError('Недостаточно средств для оплаты')
        print(f'Оплата с наличного счета на сумму {sum} рублей')
        self.balance -= sum

    def writeoff(self, sum: int):
        if self.balance < sum:
            raise PaymentError('Недостаточно средств для вывода средств вручную')
        print(f'Списание с наличного счета на сумму {sum} рублей')
        self.balance -= sum

    def accrue(self, sum: int):
        print(f'Начисление на наличный счет на сумму {sum} рублей')
        self.balance += sum
       

# Бонусный счет
class BonusAccount(BaseAccount,IPayment,IAccumulation):

    def pay(self, sum: int):
        if self.balance < sum:
            raise PaymentError('Недостаточно средств для оплаты')
        print(f'Оплата с бонусного счета на сумму {sum} рублей')
        self.balance -= sum

    def accrue(self, sum: int):
        print(f'Начисление на бонусный счет на сумму {sum} рублей')
        self.balance += sum


class TotalSpentAccount(BaseAccount,IAccumulation):

    def accrue(self, sum: int):
        print(f'Начисление на счет потрат на сумму {sum} рублей')
        self.balance += sum
        