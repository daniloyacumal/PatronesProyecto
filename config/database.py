class DatabaseConnection:
    __instance = None

    def __new__(cls):
        if cls.__instance is None:
            cls.__instance = super().__new__(cls)
            cls.__instance._initialized = False
        return cls.__instance

    def __init__(self):
        if self._initialized:
            return
        self.connection = "Database Connected"
        self._initialized = True

    def get_connection(self):
        return self.connection
