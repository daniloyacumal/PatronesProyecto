from .order import Order

class LabOrder(Order):

    def __init__(self, description, base_amount, lab_type):
        super().__init__(description, base_amount)

        if not lab_type:
            raise ValueError("lab_type es obligatorio para una orden de laboratorio")

        self.lab_type = lab_type

    def get_details(self):
        return f"[LAB] {self.description} | Tipo: {self.lab_type} | Estado: {self.status}"
