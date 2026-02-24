from .observer import Observer

class PharmacyNotifier(Observer):

    def update(self, order):
        print(f"[Farmacia] Orden '{order.description}' cambió a estado {order.status}")
