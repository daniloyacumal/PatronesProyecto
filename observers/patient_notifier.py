from .observer import Observer

class PatientNotifier(Observer):

    def update(self, message):
        print(f"Paciente notificado: {message}")
