from collections import defaultdict
from typing import List, TypeVar, Generic, Dict
from dataclasses import dataclass
from abc import ABC, abstractmethod
from accounts import IPay, IAccrue, IWriteoff, ICashAccount, PaymentError, IAccount


@dataclass
class Item:
    name: str
    price: int
    quantity: int


T = TypeVar('T')

class IBinding(ABC, Generic[T]):
    def __init__(self, account: T, sum: int):
        self.__account__ = account
        self.__sum__ = sum
        self.__committed__ = False

    @property
    def committed(self) -> bool:
        return self.__committed__

    @property
    def account(self) -> T:
        return self.__account__

    @property
    def sum(self) -> int:
        return self.__sum__
    
    @abstractmethod
    def do_commit(self):
        ...

    def commit(self):
        if not self.__committed__:
            self.do_commit()
            self.__committed__ = True

class PayBinding(IBinding[IPay]):

    @property
    def accrual_base(self) -> int:
        return self.__sum__ if isinstance(self.__account__, ICashAccount) else 0
    
    def do_commit(self):
        self.__account__.pay(self.__sum__)
    

class AccrueBinding(IBinding[IAccrue]):

    def do_commit(self):
        self.__account__.accrue(self.__sum__)
    
    
class WriteoffBinding(IBinding[IWriteoff]):

    def do_commit(self):
        self.__account__.writeoff(self.__sum__)


class Transaction:

    def __init__(self) -> None:
        self.__items__: List[Item] = None
        self.__bindings__: List[IBinding] = None
        
    @property
    def transaction_sum(self) -> int:
        return sum(item.quantity*item.price for item in self.items)
    
    @property
    def items(self) -> List[Item]:
        return self.__items__

    @property
    def bindings(self) -> List[IBinding]:
        return self.__bindings__
    
    def set_bindings(self, bindings: List[IBinding]):
        self.__bindings__ = bindings

    def set_items(self, items: List[Item]):
        self.__items__ = items

    def validate(self):
        if len(self.items) == 0:
            raise PaymentError('Попытка провести транзакцию без основания')
        
        if len(self.bindings) == 0:
            raise PaymentError('Попытка провести транзакцию без привязки счетов')
        
        total_writeoffs: Dict[IAccount, int] = defaultdict(lambda: 0)
        
        for b in self.__bindings__:
            if b.committed: continue
            if isinstance(b, (PayBinding, WriteoffBinding)):
                total_writeoffs[b.account] += b.sum

        for account, total in total_writeoffs.items():
            if account.balance < total:
                raise PaymentError('Недостаточно средств')
            
        if self.transaction_sum > sum(total_writeoffs.values()):
            raise PaymentError(f'Транзакция не сбалансирована')
    

class BindingBuilder:
    
    def __init__(self, transaction: Transaction, bonus_percent: int):
        self.__transaction__ = transaction
        self.__bindings__: List[IBinding] = []
        self.__bonus_percent__ = bonus_percent

    def add_payment(self, payment_account: IPay, bonus_account: IAccrue, total_spent_account: IAccrue, sum: int = None):
        bnd = PayBinding(payment_account, sum or self.__transaction__.transaction_sum)
        self.__bindings__.append(bnd)
        accrual_base = bnd.accrual_base
        if accrual_base > 0:
            self.__bindings__.append(AccrueBinding(bonus_account, round(accrual_base * (self.__bonus_percent__ / 100))))
            self.__bindings__.append(AccrueBinding(total_spent_account, accrual_base))
        
        return self
        
    def add_accrual(self, account: IAccrue, sum: int):
        self.__bindings__.append(AccrueBinding(account, sum))
        return self

    def add_writeoff(self, account: IWriteoff, sum: int):
        self.__bindings__.append(WriteoffBinding(account, sum))
        return self

    def build(self) -> Transaction:
        self.__transaction__.set_bindings(self.__bindings__)
        return self.__transaction__

    

class TransactionBuilder:

    def __init__(self, transaction: Transaction, bonus_percent: int):
        self.__items__: List[Item] = []
        self.__bonus_percent__ = bonus_percent
        self.__transaction__ = transaction

    def add_item(self, item: Item):
        self.__items__.append(item)
        return self
    
    def build_bindings(self) -> BindingBuilder:
        self.__transaction__.set_items(self.__items__)
        return BindingBuilder(self.__transaction__, self.__bonus_percent__)
    

class Notification:
    def __init__(self, text: str):
        self.__text__ = text

    def send(self, citizen: 'Citizen'):
        print(f'>> Привет, {citizen.name}!\n'+'>> '.join(self.__text__.splitlines(True)))
    

class Notifier:

    def notify(self, greetings: str, transaction: Transaction) -> Notification:
        text = f'>>{greetings}\n'
        text += f'{"-":-^40}\n'
        for item in transaction.__items__:
            text += f'{item.name:<30}'+f'{item.quantity * item.price:>9}\n'
        text += f'{"-":-^40}\n'
        text += f'Итого: {transaction.transaction_sum:>32}\n'
        text += f'{"-":-^40}\n'
        for binding in transaction.__bindings__:
            if isinstance(binding, PayBinding):
                text += f'Оплачено {binding.sum:.2f} со счета {binding.account.__class__.__name__}\n'
            elif isinstance(binding, AccrueBinding):
                text += f'Начислено {binding.sum:.2f} на счет {binding.account.__class__.__name__}\n'
            elif isinstance(binding, WriteoffBinding):
                text += f'Списано {binding.sum:.2f} со счета{binding.account.__class__.__name__}\n'
        text += f'{"-":-^40}\n'

        return Notification(text)


class IPaymentTerminal(ABC):
    
    def __init__(self):
        ...
 

    @abstractmethod
    def new_transaction(self) -> TransactionBuilder:
        ...

    @abstractmethod
    def commit_transaction(self, transaction: Transaction, citizen: 'Citizen'):
        ...


class TerminalMixin(IPaymentTerminal):

    def __init__(self, notifier: Notifier):
        self.__notifier__ = notifier

    def do_commit_transaction(self, transaction: Transaction):
        transaction.validate()
        [binding.commit() for binding in transaction.bindings]


# Платежный терминал в кафе
class CafeTerminal(TerminalMixin):
    
    def new_transaction(self) -> TransactionBuilder:
        return TransactionBuilder(
            Transaction(),
            10
        )
    
    def commit_transaction(self, transaction: Transaction, citizen: 'Citizen'):
        self.do_commit_transaction(transaction)
        notification = self.__notifier__.notify('Добро пожаловать в кафе!', transaction)
        notification.send(citizen)


# Платежный терминал в кинотеатре
class CinemaTerminal(TerminalMixin):

    def new_transaction(self) -> TransactionBuilder:
        return TransactionBuilder(
            Transaction(),
            15
        )
    
    def commit_transaction(self, transaction: Transaction, citizen: 'Citizen'):
        self.do_commit_transaction(transaction)
        notification = self.__notifier__.notify('Добро пожаловать в кинотеатр!', transaction)
        notification.send(citizen)

# Платежный терминал в комунальном сервисе
class UtilityServiceTerminal(TerminalMixin):

    def new_transaction(self) -> TransactionBuilder:
        return TransactionBuilder(
            Transaction(),
            0
        )
    
    def commit_transaction(self, transaction: Transaction, citizen: 'Citizen'):
        self.do_commit_transaction(transaction)
        notification = self.__notifier__.notify('Молодой человек, очередь не задерживаем!', transaction)
        notification.send(citizen)

# Палтежный терминал на работе
class JobTerminal(TerminalMixin):
    
    def new_transaction(self) -> TransactionBuilder:
        return TransactionBuilder(
            Transaction(),
            0
        )
    
    def commit_transaction(self, transaction: Transaction, citizen: 'Citizen'):
        self.do_commit_transaction(transaction)
        notification = self.__notifier__.notify('Молодец, хорошо работаешь!', transaction)
        notification.send(citizen)
        
from citizen import Citizen