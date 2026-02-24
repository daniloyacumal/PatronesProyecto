from config.database import DatabaseConnection
from factory.order_factory import OrderFactory
from strategies.eps_strategy import EPSStrategy
from observers.patient_notifier import PatientNotifier
from observers.pharmacy_notifier import PharmacyNotifier
from observers.doctor_notifier import DoctorNotifier

# Singleton
db1 = DatabaseConnection()
db2 = DatabaseConnection()

print(db1.get_connection())
print(db1 is db2)  # True

# Factory
order = OrderFactory.create_order("lab", "Examen de sangre", 100000)

# Strategy
strategy = EPSStrategy()
final_cost = strategy.calculate(order.base_amount)
print("Costo final:", final_cost)

# Observer
order.attach(PatientNotifier())
order.attach(PharmacyNotifier())
order.attach(DoctorNotifier())

order.change_status("APPROVED")
