from citizen import Citizen
from terminals.terminals import JobTerminal, CafeTerminal, CinemaTerminal, UtilityServiceTerminal
from accounts.accounts import CashAccount, BonusAccount, TotalSpentAccount

if __name__ == "__main__":

    job_terminal = JobTerminal()
    utility_terminal = UtilityServiceTerminal()
    cinema_terminal = CinemaTerminal()
    cafe_terminal = CafeTerminal()


    # Жил-был Джон
    john_doe = Citizen('Jonh Doe', CashAccount(), BonusAccount(), TotalSpentAccount())

    # Пришел Джон на работу за зарплатой
    job_terminal.dispatch_operation(john_doe, 800)

    # Оплатил комуналку
    utility_terminal.dispatch_operation(john_doe, 200)

    # Сходил в кино
    cinema_terminal.dispatch_operation(john_doe, 300)

    # И поужинал в кафе
    cafe_terminal.dispatch_operation(john_doe, 45, True)
    
    # И осталось у джона столько вот денег
    print(john_doe.get_balance())
    