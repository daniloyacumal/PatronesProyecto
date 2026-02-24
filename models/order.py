class Order:

    def __init__(self, description, base_amount):
        self.description = description
        self.base_amount = base_amount
        self.observers = []
        self.status = "CREATED"

    def attach(self, observer):
        self.observers.append(observer)

    def notify(self):
        for observer in self.observers:
            observer.update(f"Orden {self.description} cambió a {self.status}")

    def change_status(self, status):
        self.status = status
        self.notify()
