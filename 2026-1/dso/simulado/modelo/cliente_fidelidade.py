from cliente import Cliente

class ClienteFidelidade(Cliente):
    def __init__(self, codigo_fidelidade: int, desconto: float, cpf: str, nome: str, endereco: str, telefone: str):
        super().__init__()
        self.__codigo_fidelidade = codigo_fidelidade
        self.__desconto = desconto
        self.__cpf = cpf
        self.__nome = nome
        self.__endereco = endereco
        self.__telefone = telefone

    # codigo_fidelidade
    @property
    def codigo_fidelidade(self):
        return self.__codigo_fidelidade
    
    @codigo_fidelidade.setter
    def codigo_fidelidade(self, codigo_fidelidade):
        self.__codigo_fidelidade = codigo_fidelidade
    
    # desconto
    @property
    def desconto(self):
        return self.__desconto
    
    @desconto.setter
    def desconto(self, desconto):
        self.__desconto = desconto

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
