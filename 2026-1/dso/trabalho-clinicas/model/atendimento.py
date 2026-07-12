from __future__ import annotations
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from model.pagamento import Pagamento
    from model.clinica import Clinica
    from model.paciente import Paciente
    from model.profissional import Profissional
    from model.procedimento import Procedimento
    from model.tipo_atendimento import TipoAtendimento

class Atendimento:
    STATUS_AGENDADO = "agendado"
    STATUS_CANCELADO = "cancelado"

    def __init__(
        self,
        data: str,
        horario_inicio: str,
        horario_fim: str, 
        valor: float,
        clinica: "Clinica",
        paciente: "Paciente",
        profissional: "Profissional",
        tipo_atendimento: "TipoAtendimento",
    ):
        self.__data = data
        self.__horario_inicio = horario_inicio
        self.__horario_fim = horario_fim
        self.__valor = valor
        self.__clinica = clinica
        self.__paciente = paciente
        self.__profissional = profissional
        self.__tipo_atendimento = tipo_atendimento
        self.__status = self.STATUS_AGENDADO
        self.__procedimentos: list["Procedimento"] = []
        self.__pagamentos: list["Pagamento"] = []

    @property
    def data(self):
        return self.__data
    
    @property
    def horario_inicio(self):
        return self.__horario_inicio
    
    @property
    def horario_fim(self):
        return self.__horario_fim
    
    @property
    def valor(self):
        return self.__valor
    
    @property
    def clinica(self):
        return self.__clinica
    
    @property
    def paciente(self):
        return self.__paciente
    
    @property
    def profissional(self):
        return self.__profissional
    
    @property
    def tipo_atendimento(self):
        return self.__tipo_atendimento
    
    @property
    def procedimentos(self):
        return list(self.__procedimentos)
    
    @property
    def pagamentos(self):
        return list(self.__pagamentos)

    @property
    def status(self):
        return self.__status
    
    @data.setter
    def data(self, data: str):
        self.__data = data

    @horario_inicio.setter
    def horario_inicio(self, horario_inicio: str):
        self.__horario_inicio = horario_inicio

    @horario_fim.setter
    def horario_fim(self, horario_fim: str):
        self.__horario_fim = horario_fim

    @valor.setter
    def valor(self, valor: float):
        self.__valor = valor
    
    @clinica.setter
    def clinica(self, clinica: "Clinica"):
        self.__clinica = clinica
    
    @paciente.setter
    def paciente(self, paciente: "Paciente"):
        self.__paciente = paciente
    
    @profissional.setter
    def profissional(self, profissional: "Profissional"):
        self.__profissional = profissional
    
    @tipo_atendimento.setter
    def tipo_atendimento(self, tipo_atendimento: "TipoAtendimento"):
        self.__tipo_atendimento = tipo_atendimento

    def validar_horario(self) -> bool:
        try:
            return self.__horario_inicio < self.__horario_fim
        except Exception:
            return False

    def agendar(self):
        self.__status = self.STATUS_AGENDADO

    def cancelar(self):
        # Marca o atendimento como cancelado, sem apagar o histórico
        self.__status = self.STATUS_CANCELADO

    def esta_cancelado(self) -> bool:
        return self.__status == self.STATUS_CANCELADO

    def adicionar_procedimento(self, procedimento: Procedimento):
        # Lista de procedimentos, onde cada procedimento tem um custo, e o valor do atendimento é atualizado com base no custo do procedimento e no valor base do tipo de atendimento
        self.__procedimentos.append(procedimento)

    def adicionar_pagamento(self, pagamento: Pagamento):
        self.__pagamentos.append(pagamento)

    def remover_procedimento(self, procedimento: Procedimento):
        # Remove um procedimento da lista interna do atendimento, para que
        # o valor total volte a refletir apenas os procedimentos ainda válidos.
        if procedimento in self.__procedimentos:
            self.__procedimentos.remove(procedimento)

    def remover_pagamento(self, pagamento: Pagamento):
        # Remove um pagamento da lista interna do atendimento, para que
        # o valor restante volte a refletir apenas os pagamentos ainda válidos.
        if pagamento in self.__pagamentos:
            self.__pagamentos.remove(pagamento)

    def calcular_valor_total(self) -> float:
        custo_procedimentos = sum(p.calcular_custo() for p in self.__procedimentos)
        return self.__valor + custo_procedimentos

    def calcular_valor_restante(self) -> float:
        total_pago = sum(p.valor_pago for p in self.__pagamentos)
        return self.calcular_valor_total() - total_pago

    def verificar_pagamento_pendente(self) -> bool:
        return self.calcular_valor_restante() > 0
