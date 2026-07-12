from DAOs.dao import DAO
from model.tipo_atendimento import TipoAtendimento

class TipoAtendimentoDAO(DAO):
    def __init__(self):
        super().__init__('tipos_atendimento.pkl')

    def add(self, tipo: TipoAtendimento):
        if (tipo is not None) and isinstance(tipo, TipoAtendimento) and isinstance(tipo.nome, str):
            super().add(tipo.nome, tipo)

    def update(self, tipo: TipoAtendimento):
        if (tipo is not None) and isinstance(tipo, TipoAtendimento) and isinstance(tipo.nome, str):
            super().update(tipo.nome, tipo)

    def get(self, key: str):
        return super().get(key)

    def remove(self, key: str):
        return super().remove(key)
