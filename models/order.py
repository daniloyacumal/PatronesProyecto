class Order:

    def __init__(self, description, base_amount):
        self.description = description
        self.base_amount = base_amount
        self.observers = []
        self.status = "CREADO"
        self.payment_strategy = None

    # ===== Observer =====
    def attach(self, observer):
        self.observers.append(observer)

    def detach(self, observer):
        self.observers.remove(observer)

    def notify(self):
        for observer in self.observers:
            observer.update(self)

    def change_status(self, status):
        self.status = status
        self.notify()

    # ===== Strategy =====
    def set_payment_strategy(self, strategy):
        self.payment_strategy = strategy

    def calculate_final_cost(self):
        if not self.payment_strategy:
            raise Exception("No se ha definido una estrategia de pago.")
        return self.payment_strategy.calculate(self.base_amount)
