class PagamentoException(Exception):
    def __init__(self, message="Erro ao lidar com Pagamento"):
        super().__init__(message)
