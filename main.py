from citizen import Citizen
from terminals import JobTerminal, CafeTerminal, CinemaTerminal, UtilityServiceTerminal

if __name__ == "__main__":

    # Жил-был Джон
    john_doe = Citizen('Jonh Doe')

    # # Пришел Джон на работу за зарплатой
    # JobTerminal(0).dispatch_operation(john_doe, 'Jonh Doe')
    JobTerminal(john_doe).process_cash_operation(john_doe.salary)

    # # Оплатил комуналку
    # UtilityServiceTerminal(100).dispatch_operation(john_doe)
    UtilityServiceTerminal(john_doe).process_cash_operation(100)
    # # Сходил в кино
    # CinemaTerminal(100).dispatch_operation(john_doe)
    CinemaTerminal(john_doe).process_cash_operation(100)

    # # И поужинал в кафе
    # CafeTerminal(100).dispatch_operation(john_doe)
    CafeTerminal(john_doe).process_bonus_operation(100)

    # И осталось у джона столько вот денег
    john_doe.get_balance()
    