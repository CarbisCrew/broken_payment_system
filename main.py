from citizen import Citizen
from terminals.terminals import JobTerminal, CafeTerminal, CinemaTerminal, UtilityServiceTerminal
from accounts.accounts import CashAccount, BonusAccount, TotalSpentAccount
from accounts.exceptions import PaymentError
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
    try:
        utility_terminal.dispatch_operation(john_doe, 200)
    except PaymentError:
        print('На счете не достаточно средств.')

    # Сходил в кино
    try:
        cinema_terminal.dispatch_operation(john_doe, 300)
    except PaymentError:
        print('На счете не достаточно средств.')

    # И поужинал в кафе
    try:
        cafe_terminal.dispatch_operation(john_doe, 45, use_bonus=True)
    except PaymentError:
        print('На счете не достаточно средств.')

    # И осталось у джона столько вот денег
    print(john_doe.get_balance())
    