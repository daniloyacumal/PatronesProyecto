from .payment_strategy import PaymentStrategy

class EPSStrategy(PaymentStrategy):

    def calculate(self, base_amount):
        return base_amount * 0.1  # Copago 10%
