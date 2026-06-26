class Cliente():
    def __init__(self, cpf: str, nome: str, endereco: str, telefone: str):
        self.__cpf = cpf
        self.__nome = nome
        self.__endereco = endereco
        self.__telefone = telefone
    
    # cpf
    @property
    def cpf(self):
        return self.__cpf
    
    @cpf.setter
    def cpf(self, cpf):
        self.__cpf = cpf
    
    # nome
    @property
    def nome(self):
        return self.__nome
    
    @nome.setter
    def nome(self, nome):
        self.__nome = nome

    # endereco
    @property
    def endereco(self):
        return self.__endereco
    
    @endereco.setter
    def endereco(self, endereco):
        self.__endereco = endereco
    
    # telefone
    @property
    def telefone(self):
        return self.__telefone
    
    @telefone.setter
    def telefone(self, telefone):
        self.__telefone = telefone
