"""
    Estou pensando na idea de implementar uma classe abstrata para pagamento, pois existe 3 tipos diferentes 
    de pagamento, e cada um tem suas peculiaridades, como por exemplo,

    as funções vao ser implementadas com base na variavel tipo_pagamento que pode ser "dinheiro", "cartao_credito" ou 
    "cartao_debito", e cada função vai ter uma lógica diferente para cada tipo de pagamento.
"""

from __future__ import annotations # Import para evitar problemas de importação em loop, pois a classe Pagamento vai precisar importar a classe Atendimento, e a classe Atendimento vai precisar importar a classe Pagamento, e isso pode causar um erro de importação em loop, então com esse import, isso é evitado.
from abc import ABC, abstractmethod
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from model.atendimento import Atendimento

class Pagamento(ABC):
    def __init__(
        self,
        data: str,
        valor_pago: float,
    ):
        self.__data = data
        self.__valor_pago = valor_pago

    @property
    def data(self):
        return self.__data

    @property
    def valor_pago(self):
        return self.__valor_pago

    @data.setter
    def data(self, data: str):
        self.__data = data

    @valor_pago.setter
    def valor_pago(self, valor_pago: float):
        self.__valor_pago = valor_pago

    @abstractmethod
    def realizar_pagamento(self, atendimento: "Atendimento") -> bool:
        pass

    @abstractmethod
    def validar_pagamento(self, atendimento: "Atendimento") -> bool:
        pass

    @abstractmethod
    def calcular_saldo(self, atendimento: "Atendimento") -> float:
        pass
