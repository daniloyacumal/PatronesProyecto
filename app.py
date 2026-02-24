from factory.order_factory import OrderFactory
from strategies.eps_strategy import EPSStrategy
from observers.patient_notifier import PatientNotifier
from observers.pharmacy_notifier import PharmacyNotifier
from observers.doctor_notifier import DoctorNotifier

# Crear orden de laboratorio
order = OrderFactory.create_order(
    order_type="lab",
    description="Examen de sangre",
    base_amount=100000,
    lab_type="Hematología"
)

print(order.get_details())

# Strategy
strategy = EPSStrategy()
final_cost = strategy.calculate(order.base_amount)
print("Costo final:", final_cost)

# Observer
order.attach(PatientNotifier())
order.attach(PharmacyNotifier())
order.attach(DoctorNotifier())

order.change_status("APROBADO")
