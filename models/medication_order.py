from .order import Order

class MedicationOrder(Order):

    def __init__(self, description, base_amount, dosage):
        super().__init__(description, base_amount)
        self.dosage = dosage

    def get_details(self):
        return f"Orden de Medicamento: {self.description} - Dosis: {self.dosage}"
