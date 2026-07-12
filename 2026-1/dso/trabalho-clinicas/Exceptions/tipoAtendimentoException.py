
class TipoAtendimentoException(Exception):
    def __init__(self, message="Erro ao lidar com Tipo de Atendimento"):
        super().__init__(message)
