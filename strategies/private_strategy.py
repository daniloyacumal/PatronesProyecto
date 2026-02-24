from .payment_strategy import PaymentStrategy

class PrivateStrategy(PaymentStrategy):

    def calculate(self, base_amount):
        return base_amount
