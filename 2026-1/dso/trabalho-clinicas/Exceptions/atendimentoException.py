
class AtendimentoException(Exception):
    def __init__(self, message="Erro ao lidar com Atendimento"):
        super().__init__(message)
