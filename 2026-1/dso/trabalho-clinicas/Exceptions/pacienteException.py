
class PacienteException(Exception):
    def __init__(self, message="Erro ao lidar com Paciente"):
        super().__init__(message)
