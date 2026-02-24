from models.lab_order import LabOrder
from models.medication_order import MedicationOrder
from models.procedure_order import ProcedureOrder

class OrderFactory:

    @staticmethod
    def create_order(order_type, description, base_amount, **kwargs):

        if order_type == "lab":
            return LabOrder(description, base_amount, kwargs.get("lab_type"))

        elif order_type == "medication":
            return MedicationOrder(description, base_amount, kwargs.get("dosage"))

        elif order_type == "procedure":
            return ProcedureOrder(description, base_amount, kwargs.get("complexity_level"))

        else:
            raise ValueError("Tipo de orden no válido")
