from abc import ABC, abstractmethod

class IBalance(ABC):

    def __init__(self, initial_balance: int = 0) -> None:
        self.__balance__ = initial_balance

    @property
    def balance(self) -> int:
        return self.__balance__
    
    def __iadd__(self, sum):
        self.__balance__ += sum
    
    def __isub__(self, sum):
        self.__balance__ -= sum

class IPay(ABC):
    
    @abstractmethod
    def pay(self, sum: int):
        pass

class IWriteOff(ABC):
    
    @abstractmethod
    def write_off(self, sum: int):
        pass

class IAccrue(ABC):
    
    @abstractmethod
    def accrue(self, sum: int):
        pass