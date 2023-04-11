from product import Product
from accounts import UserAccount
from invoice import Invoice

if __name__ == "__main__":
    john_doe = UserAccount()
    john_doe.accrue(500, 'Зачисление заработной платы', 'cash')
    john_doe.pay(70, 'cash') # Комунальные платежи

    Invoice()\
        .add_product(Product(
            name='Вареники с вишней',
            count=1,
            price=100
        ))\
        .add_product(Product(
            name='Эспрессо',
            count=2,
            price=50
        ))\
        .add_product(Product(
            name='Добавка: Молоко',
            count=1,
            price=25
        ))\
        .pay_invoice(john_doe.cash)
    
    print(john_doe.cash.balance)
    print(john_doe.bonus.balance)
    print(john_doe.spent.balance)
    