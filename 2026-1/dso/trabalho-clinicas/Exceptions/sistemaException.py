
class SistemaException(Exception):
    def __init__(self, message="Erro no Sistema"):
        super().__init__(message)
