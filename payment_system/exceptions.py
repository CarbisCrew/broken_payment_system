class PaymentError(Exception):
    """Стандартное исключение платежной системы"""
    ...


class BalanceBelowZeroError(PaymentError):
    """Исключение для баланса ниже нуля"""
    ...


class PayError(PaymentError):
    """Исключение для ошибки оплаты"""
    ...


class WriteOffError(PaymentError):
    """Исключение для ошибки ручного списания"""
    ...
