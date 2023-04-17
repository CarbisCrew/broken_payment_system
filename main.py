from citizen import Citizen
from terminals import JobTerminal,CafeTerminal,UtilityServiceTerminal,CinemaTerminal
from accounts import CashAccount, BonusAccount,TotalSpentAccount
if __name__ == "__main__":

    # Жил-был Джон
    john_doe = Citizen(cash_account=CashAccount(),bonus_account=BonusAccount(),total_spent_account=TotalSpentAccount())

    # Пришел Джон на работу за зарплатой
    JobTerminal().dispatch_operation(john_doe, 'Jonh Doe')
# #     # Оплатил комуналку
    UtilityServiceTerminal(800).dispatch_operation(john_doe)

# #     # Сходил в кино
#     CinemaTerminal(100).dispatch_operation(john_doe,john_doe.cash_account)

#     # И поужинал в кафе
#     CafeTerminal(10).dispatch_operation(john_doe,john_doe.bonus_account)
    
#     # И осталось у джона столько вот денег
    print(john_doe.cash_account.balance)
    print(john_doe.bonus_account.balance)
    print(john_doe.total_spent_account.balance)

