from .observer import Observer

class PharmacyNotifier(Observer):

    def update(self, message):
        print(f"Farmacia notificada: {message}")
