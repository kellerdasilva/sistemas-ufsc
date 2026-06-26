class ItemPedido():
    def __init__(self, codigo: int, descricao: str, preco_unitario: float):
        self.__codigo = codigo
        self.__descricao = descricao
        self.__preco_unitario = preco_unitario
    
    # codigo
    @property
    def codigo(self):
        return self.__codigo
    
    @codigo.setter
    def codigo(self, codigo):
        self.__codigo = codigo
    
    # descricao
    @property
    def descricao(self):
        return self.__descricao
    
    @descricao.setter
    def descricao(self, descricao):
        self.__descricao = descricao
    
    # preco_unitario
    @property
    def preco_unitario(self):
        return self.__preco_unitario
    
    @preco_unitario.setter
    def preco_unitario(self, preco_unitario):
        self.__preco_unitario = preco_unitario