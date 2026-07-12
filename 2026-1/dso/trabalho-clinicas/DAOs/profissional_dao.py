from DAOs.dao import DAO
from model.profissional import Profissional

class ProfissionalDAO(DAO):
    def __init__(self):
        super().__init__('profissionais.pkl')

    def add(self, profissional: Profissional):
        if (profissional is not None) and isinstance(profissional, Profissional) and isinstance(profissional.cpf, str):
            super().add(profissional.cpf, profissional)

    def update(self, profissional: Profissional):
        if (profissional is not None) and isinstance(profissional, Profissional) and isinstance(profissional.cpf, str):
            super().update(profissional.cpf, profissional)

    def get(self, key: str):
        return super().get(key)

    def remove(self, key: str):
        return super().remove(key)
