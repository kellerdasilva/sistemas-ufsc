from modelo.pedido_duplicado_exception import PedidoDuplicadoException
from modelo.pedido import Pedido

class ControladorPedidos():
    def __init__(self):
        self.__pedidos = []
    
    def incluir_pedido(self, pedido):
    # Incluir pedido na lista.
    # Tratar os casos de instancias incorretas e pedido duplicado.
    # Caso o pedido já exista na lista, gerar a excecao: 
    # PedidoDuplicadoException
        pass
    
    def busca_pedido_por_numero(self, numero):
    # Busca pedido pelo numero.
    # Se o pedido nao existir, deve retornar None
    # Caso contrario, retorna o pedido.
        pass
    
    def excluir_pedido(self, numero):
    # Exclui pedido pelo numero.
    # Se o pedido nao existir, deve retornar None
    # Caso contrario, retorna o pedido excluido
        pass
    
    def calcular_faturamento_pedidos(distancia, cpf):
    # Deve calcular o total do faturamento para todos os
    # itens pedidos por um CPF. 
    # Recebe como parametro:
    # distancia: um float que corresponde a distancia percorrida
    # cpf: uma string representando o CPF do Cliente a ser faturado
        pass