from .order import Order

class LabOrder(Order):

    def __init__(self, description, base_amount, lab_type):
        super().__init__(description, base_amount)
        self.lab_type = lab_type

    def get_details(self):
        return f"Orden de Laboratorio: {self.description} - Tipo: {self.lab_type}"
