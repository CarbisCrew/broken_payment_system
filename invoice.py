from typing import List
from accounts import IAccount
from product import Product

class Invoice:
    def __init__(self) -> None:
        self.__goods__: List[Product] = []

    def add_product(self, product: Product):
        self.__goods__.append(product)
        return self

    @property
    def invoice_total(self) -> int:
        return sum(product.sum for product in self.__goods__)

    def pay_invoice(self, account: IAccount):
        account.pay(self.invoice_total)