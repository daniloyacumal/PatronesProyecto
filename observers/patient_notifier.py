from .observer import Observer

class PatientNotifier(Observer):

    def update(self, order):
        print(f"[Paciente] Orden '{order.description}' cambió a estado {order.status}")
