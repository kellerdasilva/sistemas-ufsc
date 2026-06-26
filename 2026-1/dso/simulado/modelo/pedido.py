from cliente import Cliente
from tipo_pedido import TipoPedido
from item_pedido import ItemPedido
from cliente_fidelidade import ClienteFidelidade

class Pedido():
    def __init__(self, numero: int, cliente: Cliente, tipo: TipoPedido):
        self.__numero = numero
        self.__cliente = cliente
        self.__tipo = tipo
        self.__itens = []
    
    # numero
    @property
    def numero(self):
        return self.__numero
    
    @numero.setter
    def numero(self, numero):
        self.__numero = numero
    
    # cliente
    @property
    def cliente(self):
        return self.__cliente
    
    @cliente.setter
    def cliente(self, cliente):
        self.__cliente = cliente
    
    # tipo
    @property
    def tipo(self):
        return self.__tipo
    
    @tipo.setter
    def tipo(self, tipo):
        self.__tipo = tipo
    
    # itens
    @property
    def itens(self):
        return self.__itens
    
    @itens.setter
    def itens(self, itens):
        self.__itens = itens
    
    def calcula_valor_pedido(distancia):
    # Deve calcular o valor total do pedido, considerando um custo
    # adicional pela distancia e fator por distancia percorrida. 
    # O fator da distancia varia de acordo com o tipo de pedido.
    # O fator_distancia do TipoPedido deve ser multiplicado pela distancia 
    # e acrescido ao valor total dos itens. 
    # Por exemplo, se o fator_distancia for 2 e a distancia for 5, 
    # o total do pedido deve ser acrescido em 10. 
    # Ainda, se o cliente for ClienteFidelidade, deve  diminuir o valor total 
    # pelo percentual de desconto armazenado no atributo desconto do ClienteFidelidade. 
    # Por exemplo, se o valor de desconto for 0.2 e o pedido custar 10, o desconto deve ser
    # de 2 e o valor final 8.
    # @return um float correspondente ao total do pedido
        pass
    
    def inclui_item_pedido(codigo, descricao, preco):
    # Inclui um novo item na lista de itens do pedido.
    # Nao deve ser possivel incluir itens duplicados (com o mesmo codigo).
    # Retornar o item incluido em caso de sucesso e None em caso
    # de item duplicado.
        pass
    
    def excui_item_pedido(codigo):
    # Exclui um item do pedido e retorna o item excluido
    # Caso o item nao exista, retorne None
        pass
