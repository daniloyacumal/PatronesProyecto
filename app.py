from config.database import DatabaseConnection
from factory.order_factory import OrderFactory
from strategies.eps_strategy import EPSStrategy
from strategies.private_strategy import PrivateStrategy
from observers.patient_notifier import PatientNotifier
from observers.pharmacy_notifier import PharmacyNotifier
from observers.doctor_notifier import DoctorNotifier

def main():

    # ===== Singleton =====
    db1 = DatabaseConnection()
    db2 = DatabaseConnection()

    print(db1.get_connection())
    print("¿Misma instancia?:", db1 is db2)

    # ===== Factory =====
    order = OrderFactory.create_order(
        order_type="lab",
        description="Examen de sangre",
        base_amount=100000,
        lab_type="Hematología"
    )

    print(order.get_details())

    # ===== Strategy =====
    order.set_payment_strategy(EPSStrategy())
    final_cost = order.calculate_final_cost()
    print("Costo final:", final_cost)

    # ===== Observer =====
    order.attach(PatientNotifier())
    order.attach(PharmacyNotifier())
    order.attach(DoctorNotifier())

    order.change_status("APROBADO")

if __name__ == "__main__":
    main()
