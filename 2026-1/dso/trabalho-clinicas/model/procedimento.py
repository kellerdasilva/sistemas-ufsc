from __future__ import annotations
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from model.profissional import Profissional

class Procedimento:
    def __init__(self, descricao: str, custo: float, profissional_responsavel: "Profissional"):
        self.__descricao = descricao
        self.__custo = custo
        self.__profissional_responsavel = profissional_responsavel

    @property
    def descricao(self):
        return self.__descricao

    @property
    def custo(self):
        return self.__custo

    @property
    def profissional_responsavel(self):
        return self.__profissional_responsavel
    
    @descricao.setter
    def descricao(self, descricao: str):
        self.__descricao = descricao

    @custo.setter
    def custo(self, custo: float):
        self.__custo = custo
    
    @profissional_responsavel.setter
    def profissional_responsavel(self, profissional: "Profissional"):
        self.__profissional_responsavel = profissional

    def calcular_custo(self) -> float:
        # Retorna o custo do procedimento
        return self.__custo
