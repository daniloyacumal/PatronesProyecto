from .observer import Observer

class DoctorNotifier(Observer):

    def update(self, order):
        print(f"[Médico] Orden '{order.description}' cambió a estado {order.status}")
