from __future__ import annotations
from model.pagamento import Pagamento
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from model.atendimento import Atendimento

class PagamentoDinheiro(Pagamento):
    def __init__(self, data: str, valor_pago: float):
        super().__init__(data, valor_pago)

    def realizar_pagamento(self, atendimento: "Atendimento") -> bool:
        # Realiza o pagamento em dinheiro se o valor for suficiente
        return self.validar_pagamento(atendimento)

    def validar_pagamento(self, atendimento: "Atendimento") -> bool:
        # Valida se o valor pago é suficiente para cobrir o atendimento
        return self.valor_pago > 0

    def calcular_saldo(self, atendimento: "Atendimento") -> float:
        # Calcula o saldo/troco após o pagamento
        return self.valor_pago - atendimento.calcular_valor_restante()
