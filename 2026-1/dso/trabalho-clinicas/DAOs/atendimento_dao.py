from DAOs.dao import DAO
from model.atendimento import Atendimento

class AtendimentoDAO(DAO):
    def __init__(self):
        super().__init__('atendimentos.pkl')

    def add(self, key: str, atendimento: Atendimento):
        if (atendimento is not None) and isinstance(atendimento, Atendimento):
            super().add(key, atendimento)

    def update(self, key: str, atendimento: Atendimento):
        if (atendimento is not None) and isinstance(atendimento, Atendimento):
            super().update(key, atendimento)

    def get(self, key: str):
        return super().get(key)

    def remove(self, key: str):
        return super().remove(key)
        
    def get_all(self):
        return super().get_all()
