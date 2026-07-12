
class TipoAtendimento:
    def __init__(self, nome ,descricao, valor_base):
        self.__nome = nome
        self.__descricao = descricao
        self.__valor_base = valor_base

    @property
    def nome(self):
        return self.__nome
    
    @property
    def descricao(self):
        return self.__descricao
    
    @property
    def valor_base(self):
        return self.__valor_base
    
    @nome.setter
    def nome(self, nome):
        self.__nome = nome
    
    @descricao.setter
    def descricao(self, descricao):
        self.__descricao = descricao
    
    @valor_base.setter
    def valor_base(self, valor_base):
        self.__valor_base = valor_base

    # metodos;
    def atualizar_valor_base(self, novo_valor):
        # o valor é atualizado com base em algum critério, por exemplo, 
        self.__valor_base = novo_valor