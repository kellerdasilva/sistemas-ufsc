from DAOs.dao import DAO
from model.clinica import Clinica

class ClinicaDAO(DAO):
    def __init__(self):
        super().__init__('clinicas.pkl')

    def add(self, clinica: Clinica):
        if (clinica is not None) and isinstance(clinica, Clinica):
            # Usando uma tupla (nome, cidade) como chave composta
            super().add((clinica.nome, clinica.cidade), clinica)

    def update(self, clinica: Clinica):
        if (clinica is not None) and isinstance(clinica, Clinica):
            super().update((clinica.nome, clinica.cidade), clinica)

    def get(self, nome: str, cidade: str):
        return super().get((nome, cidade))

    def remove(self, nome: str, cidade: str):
        return super().remove((nome, cidade))
