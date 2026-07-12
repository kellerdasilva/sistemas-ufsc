"""
Com base na arquitetura (MVC) Model-View-Controller, o módulo Clinica é responsável por representar a lógica de negócio do sistema,
ou seja, as classes e funções que definem o comportamento do sistema e como ele deve funcionar.

Clinica é o módulo principal do projeto, onde estão as classes e funções que representam a lógica de negócio do sistema.

Com base no diagrama do model, basta escrever as classes nesta pasta model
"""

from __future__ import annotations
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from model.profissional import Profissional

class Clinica:
    def __init__(self, nome: str, cidade: str, horario_abertura: str, horario_fechamento: str):
        self.__nome = nome
        self.__cidade = cidade
        self.__horario_abertura = horario_abertura
        self.__horario_fechamento = horario_fechamento
        self.__profissionais: list["Profissional"] = []

    @property
    def nome(self):
        return self.__nome
    
    @property
    def cidade(self):
        return self.__cidade
    
    @property
    def horario_abertura(self):
        return self.__horario_abertura

    @property
    def horario_fechamento(self):
        return self.__horario_fechamento

    @property
    def profissionais(self):
        return list(self.__profissionais)

    @nome.setter
    def nome(self, nome):
        self.__nome = nome

    @cidade.setter
    def cidade(self, cidade):
        self.__cidade = cidade

    @horario_abertura.setter
    def horario_abertura(self, horario_abertura):
        self.__horario_abertura = horario_abertura

    @horario_fechamento.setter
    def horario_fechamento(self, horario_fechamento):
        self.__horario_fechamento = horario_fechamento

    def esta_aberta(self, horario_atual: str) -> bool:
        return self.__horario_abertura <= horario_atual < self.__horario_fechamento
        
    def validar_horario_atendimento(self, horario_inicio: str, horario_fim: str) -> bool:
        return (
            self.esta_aberta(horario_inicio)
            and self.esta_aberta(horario_fim)
            and horario_inicio < horario_fim
        )

    def adicionar_profissional(self, profissional: "Profissional"):
        # Vincula um profissional já existente à clínica (agregação: não cria o profissional).
        if profissional not in self.__profissionais:
            self.__profissionais.append(profissional)

    def remover_profissional(self, profissional: "Profissional"):
        # Desvincula o profissional da clínica. O profissional em si continua existindo.
        if profissional in self.__profissionais:
            self.__profissionais.remove(profissional)
