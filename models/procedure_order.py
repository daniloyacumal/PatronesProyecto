from .order import Order

class ProcedureOrder(Order):

    def __init__(self, description, base_amount, complexity_level):
        super().__init__(description, base_amount)
        self.complexity_level = complexity_level

    def get_details(self):
        return f"Orden de Procedimiento: {self.description} - Complejidad: {self.complexity_level}"
