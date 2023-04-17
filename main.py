from payment_system.citizen import Citizen
from payment_system.terminals import JobTerminal, CafeTerminal, CinemaTerminal, UtilityServiceTerminal
from payment_system.accounts import CashAccount, BonusAccount, TotalSpentAccount

if __name__ == "__main__":

    # Жил-был Джон
    john_doe = Citizen(name="John Doe",
                       cash_account=CashAccount(),
                       bonus_account=BonusAccount(),
                       total_spent_account=TotalSpentAccount())

    # Пришел Джон на работу за зарплатой
    JobTerminal().process_cash_operation(john_doe)

    # Оплатил комуналку
    UtilityServiceTerminal(100).process_cash_operation(john_doe)

    # Сходил в кино
    CinemaTerminal(100).process_cash_operation(john_doe)

    # И поужинал в кафе
    CafeTerminal(100).process_cash_operation(john_doe)
    
    # И осталось у джона столько вот денег
    print(john_doe.cash_account.balance)
    print(john_doe.bonus_account.balance)
    print(john_doe.total_spent_account.balance)
    