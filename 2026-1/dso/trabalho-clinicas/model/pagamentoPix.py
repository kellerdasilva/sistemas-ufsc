from __future__ import annotations
from model.pagamento import Pagamento
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from model.atendimento import Atendimento

class PagamentoPix(Pagamento):
    def __init__(self, data: str, valor_pago: float, cpf_pagador: str):
        super().__init__(data, valor_pago)
        self.__cpf_pagador = cpf_pagador
    
    @property
    def cpf_pagador(self):
        return self.__cpf_pagador

    @cpf_pagador.setter
    def cpf_pagador(self, cpf_pagador: str):
        self.__cpf_pagador = cpf_pagador

    def realizar_pagamento(self, atendimento: "Atendimento") -> bool:
        # Realiza o pagamento via Pix se o valor for suficiente
        return self.validar_pagamento(atendimento)

    def validar_pagamento(self, atendimento: "Atendimento") -> bool:
        # Valida se o valor pago é suficiente para cobrir o atendimento
        if not (self.__cpf_pagador and len(self.__cpf_pagador) == 11 and self.__cpf_pagador.isdigit()):
            return False
        return self.valor_pago > 0
    
    def calcular_saldo(self, atendimento: "Atendimento") -> float:
        # Calcula o saldo/troco após o pagamento
        return self.valor_pago - atendimento.calcular_valor_restante()
    