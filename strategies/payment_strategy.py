from abc import ABC, abstractmethod

class PaymentStrategy(ABC):

    @abstractmethod
    def calculate(self, base_amount):
        pass
