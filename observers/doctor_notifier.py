from .observer import Observer

class DoctorNotifier(Observer):

    def update(self, message):
        print(f"Médico notificado: {message}")
