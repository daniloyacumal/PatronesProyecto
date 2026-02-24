from .payment_strategy import PaymentStrategy

class InsuranceStrategy(PaymentStrategy):

    def calculate(self, base_amount):
        return base_amount * 0.2
