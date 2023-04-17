from citizen import Citizen
from terminals import JobTerminal, CafeTerminal, CinemaTerminal, UtilityServiceTerminal
if __name__ == "__main__":

    # Жил-был Джон
    john_doe = Citizen()

    # Пришел Джон на работу за зарплатой
    JobTerminal(0).process_cash_operation(john_doe, 'Jonh Doe')
    print(john_doe.cash_account.balance)

    # Оплатил комуналку
    UtilityServiceTerminal(100).process_cash_operation(john_doe)

    # Сходил в кино
    CinemaTerminal(100).process_cash_operation(john_doe)

    # И поужинал в кафе
    CafeTerminal(100).process_cash_operation(john_doe)
    CafeTerminal(35).process_bonus_operation(john_doe)

    # И осталось у джона столько вот денег
    print(john_doe.cash_account.balance)
    print(john_doe.bonus_account.balance)
    print(john_doe.total_spent_account.balance)
    