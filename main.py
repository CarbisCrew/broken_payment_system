from citizen import Citizen
from accounts import CashAccount, BonusAccount, TotalSpentAccount
from terminals import JobTerminal, CafeTerminal, CinemaTerminal, UtilityServiceTerminal, Item, Notifier

if __name__ == "__main__":

    # Жил-был Джон
    john_doe = Citizen(
        'John Doe',
        CashAccount(),
        BonusAccount(),
        TotalSpentAccount()
    )

    notifier = Notifier()

    # Пришел Джон на работу за зарплатой
    job = JobTerminal(notifier)
    salary = job.new_transaction()\
        .add_item(Item(
            'Зачисление заработной платы',
            price=0,
            quantity=1
        )).build_bindings()\
        .add_accrual(john_doe.cash_account, len(john_doe.name) * 100)\
        .build()
    job.commit_transaction(salary, john_doe)
    
    
        

    # Оплатил комуналку
    utility_service = UtilityServiceTerminal(notifier)
    robbery = utility_service.new_transaction()\
        .add_item(Item(
            'Коммунальные услуги',
            price=100,
            quantity=1
        )).build_bindings()\
        .add_payment(john_doe.cash_account, john_doe.bonus_account, john_doe.total_spent_account, 100)\
        .add_writeoff(john_doe.cash_account, 10)\
        .build()
    utility_service.commit_transaction(robbery, john_doe)

    
    
    
    # Сходил в кино
    cinema = CinemaTerminal(notifier)
    invoice = cinema.new_transaction()\
        .add_item(Item(
            'Аватар: Путь воды',
            price=50,
            quantity=1
        ))\
        .add_item(Item(
            'Кола',
            price=50,
            quantity=1
        ))\
        .add_item(Item(
            'Попкорн',
            price=50,
            quantity=1
        )).build_bindings()\
        .add_payment(john_doe.cash_account, john_doe.bonus_account, john_doe.total_spent_account)\
        .build()
    cinema.commit_transaction(invoice, john_doe)


    # И поужинал в кафе
    cafe = CafeTerminal(notifier)
    invoice = cafe.new_transaction()\
        .add_item(Item(
            "Кофе",
            price=50,
            quantity=1
        ))\
        .add_item(Item(
            "Булочка с корицей",
            price=50,
            quantity=2
        )).build_bindings()\
        .add_payment(john_doe.bonus_account, john_doe.bonus_account, john_doe.total_spent_account, 10)\
        .add_payment(john_doe.cash_account, john_doe.bonus_account, john_doe.total_spent_account, 140)\
        .build()
    cafe.commit_transaction(invoice, john_doe)
    
    # И осталось у джона столько вот денег
    print(john_doe.cash_account.balance)
    print(john_doe.bonus_account.balance)
    print(john_doe.total_spent_account.balance)
    