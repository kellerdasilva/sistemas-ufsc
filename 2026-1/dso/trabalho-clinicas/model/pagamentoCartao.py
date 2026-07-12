from __future__ import annotations
from model.pagamento import Pagamento
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from model.atendimento import Atendimento

class PagamentoCartao(Pagamento):
    def __init__(self, data: str, valor_pago: float, numero_cartao: str, bandeira_cartao: str):
        super().__init__(data, valor_pago)
        self.__numero_cartao = numero_cartao
        self.__bandeira_cartao = bandeira_cartao

    @property
    def numero_cartao(self):
        return self.__numero_cartao
    
    @property
    def bandeira_cartao(self):
        return self.__bandeira_cartao
    
    @numero_cartao.setter
    def numero_cartao(self, numero_cartao: str):
        self.__numero_cartao = numero_cartao
        
    @bandeira_cartao.setter
    def bandeira_cartao(self, bandeira_cartao: str):
        self.__bandeira_cartao = bandeira_cartao 

    def validar_cartao(self) -> bool:
        return (
            self.__numero_cartao is not None
            and len(self.__numero_cartao) == 16
            and self.__numero_cartao.isdigit()
            and self.__bandeira_cartao is not None
            and len(self.__bandeira_cartao) > 0
        )

    def realizar_pagamento(self, atendimento: "Atendimento") -> bool:
        # Realiza o pagamento com cartão se for válido
        return self.validar_pagamento(atendimento)
    
    def validar_pagamento(self, atendimento: "Atendimento") -> bool:
        # Valida se o cartão está correto
        if not self.validar_cartao():
            return False
        return self.valor_pago > 0
    
    def calcular_saldo(self, atendimento: "Atendimento") -> float:
        # Calcula o saldo após o pagamento
        return self.valor_pago - atendimento.calcular_valor_restante()
