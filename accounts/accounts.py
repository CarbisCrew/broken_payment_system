from .exceptions import PaymentError
from .acc_interfaces import IBalance, IAccrue, IPay, IWriteOff
from typing import List, Tuple

'''Декоратор для проверки есть ли сумма на счете для списания'''
def check_sum_exists(func):
    
    def wrapper(*args: Tuple[IBalance, int], **kwargs):
    
        if args[0].balance < args[1]:
            raise PaymentError('Недостаточно средств')
        return_func = func(*args, **kwargs)
    
        return return_func

    return wrapper


# Наличный счет
class CashAccount(IBalance, IPay, IWriteOff, IAccrue):

    @check_sum_exists
    def pay(self, sum: int):
        print(f'Оплата с наличного счета на сумму {sum} рублей')
        self -= sum

    @check_sum_exists
    def write_off(self, sum: int):
        print(f'Списание с наличного счета на сумму {sum} рублей')
        self -= sum

    def accrue(self, sum: int):
        print(f'Начисление на наличный счет на сумму {sum} рублей')
        self += sum
       

# Бонусный счет
class BonusAccount(IBalance, IPay, IAccrue):

    @check_sum_exists
    def pay(self, sum: int):
        print(f'Оплата с бонусного счета на сумму {sum} рублей')
        self -= sum

    def accrue(self, sum: int):
        print(f'Начисление на бонусный счет на сумму {sum} рублей')
        self  += sum


class TotalSpentAccount(IBalance, IAccrue):

    def accrue(self, sum: int):
        print(f'Начисление на счет потрат на сумму {sum} рублей')
        self += sum
        