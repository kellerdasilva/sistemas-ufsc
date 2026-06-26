class TipoPedido():
    def __init__(self, descricao: str, fator_distancia: float):
        self.__descricao = descricao
        self.__fator_distancia = fator_distancia
        # O atributo fator_distancia eh um float que representa
        # o custo pela distancia percorrida para aquele tipo de pedido.
    
    # descricao
    @property
    def descricao(self):
        return self.__descricao
    
    @descricao.setter
    def descricao(self, descricao):
        self.__descricao = descricao
    
    # fator_distancia
    @property
    def fator_distancia(self):
        return self.__cliente
    
    @fator_distancia.setter
    def fator_distancia(self, fator_distancia):
        self.__cliente = fator_distancia