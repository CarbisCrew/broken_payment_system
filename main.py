from citizen import Citizen
from terminals import JobTerminal, CafeTerminal, CinemaTerminal, UtilityServiceTerminal
from accounts import CashAccount, BonusAccount, TotalSpentAccount

if __name__ == "__main__":

    # Жил-был Джон
    john_doe = Citizen(name='Jonh Doe',
                       cash_account=CashAccount(),
                       bonus_account=BonusAccount(),
                       total_spent_account=TotalSpentAccount())

    # Пришел Джон на работу за зарплатой
    JobTerminal(john_doe).process_cash_operation(john_doe.salary)
    # Оплатил комуналку
    UtilityServiceTerminal(john_doe).process_cash_operation(100)
    # Сходил в кино
    CinemaTerminal(john_doe).process_cash_operation(100)

    # И поужинал в кафе
    CafeTerminal(john_doe).process_bonus_operation(10)

    # И осталось у джона столько вот денег
    john_doe.get_balance()
    