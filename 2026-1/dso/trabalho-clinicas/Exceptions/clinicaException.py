
class ClinicaException(Exception):
    def __init__(self, message="Erro ao lidar com Clínica"):
        super().__init__(message)
