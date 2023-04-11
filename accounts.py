class PaymentError(Exception):
    ...

class IAccount:

    def __init__(self, initial_balance: int = 0) -> None:
        self.__balance__ = initial_balance

    @property
    def balance(self) -> int:
        return self.__balance__

    def pay(self, sum: int):
        ...

    def writeoff(self, sum: int, reason: str):
        ...

    def accrue(self, sum: int, reason: str):
        ...


class CashAccount(IAccount):
    
    def pay(self, sum: int):
        if self.balance < sum:
            raise PaymentError('На счете недостаточно средств')
        print(f'Оплата с наличного счета на сумму {sum} рублей')
        self.__balance__ -= sum

    def writeoff(self, sum: int, reason: str):
        raise PaymentError(f'Запрещено списывать средства с наличного счета')

    def accrue(self, sum: int, reason: str):
        print(f'Начисление на наличный счет на сумму {sum} рублей: {reason}')
        self.__balance__ += sum
       

class BonusAccount(IAccount):

    def pay(self, sum: int):
        if self.balance < sum:
            raise PaymentError('На счете недостаточно средств')
        print(f'Оплата с бонусного счета на сумму {sum} рублей')
        self.__balance__ -= sum

    def writeoff(self, sum: int, reason: str):
        print(f'Списание с бонусного счета на сумму {sum} рублей: {reason}')
        self.__balance__ -= sum

    def accrue(self, sum: int, reason: str):
        print(f'Начисление на бонусный счет на сумму {sum} рублей: {reason}')
        self.__balance__ += sum


class TotalSpentAccount(IAccount):

    def pay(self, sum: int):
        raise PaymentError(f'Запрещено оплачивать покупки со счета потрат')

    def writeoff(self, sum: int, reason: str):
        raise PaymentError(f'Запрещено списывать средства со счета потрат')

    def accrue(self, sum: int, reason: str):
        print(f'Начисление на счет потрат на сумму {sum} рублей: {reason}')
        self.__balance__ += sum


class UserAccount(IAccount):
    
    def __init__(self) -> None:
        self.cash = CashAccount()
        self.bonus = BonusAccount()
        self.spent = TotalSpentAccount()

    def pay(self, sum: int, payment_type: str):
        if payment_type == 'bonus':
            self.bonus.pay(sum)
        elif payment_type == 'cash':
            self.cash.pay(sum)
            self.spent.accrue(sum, 'Оплата покупки')

    def writeoff(self, sum: int, reason: str):
        self.bonus.writeoff(sum, reason)

    def accrue(self, sum: int, reason: str, account: str):
        if account == 'cash':
            self.cash.accrue(sum, reason)
        elif account == 'bonus':
            self.bonus.accrue(sum, reason)
        elif account == 'spent':
            self.spent.accrue(sum, reason)
