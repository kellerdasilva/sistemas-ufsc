
class ProfissionalException(Exception):
    def __init__(self, message="Erro ao lidar com Profissional"):
        super().__init__(message)
