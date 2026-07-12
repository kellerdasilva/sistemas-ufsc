from datetime import date
from model.pessoa import Pessoa

class Paciente(Pessoa):
    def __init__(
        self,
        nome: str,
        celular: str,
        cpf: str,
        data_nascimento: date,
        nome_responsavel: str = None,
        cpf_responsavel: str = None,
    ):
        super().__init__(nome, celular, cpf)
        self.__data_nascimento = data_nascimento
        self.__nome_responsavel = nome_responsavel
        self.__cpf_responsavel = cpf_responsavel

    @property
    def data_nascimento(self) -> date:
        return self.__data_nascimento

    @property
    def nome_responsavel(self) -> str:
        return self.__nome_responsavel

    @property
    def cpf_responsavel(self) -> str:
        return self.__cpf_responsavel

    @data_nascimento.setter
    def data_nascimento(self, data_nascimento: date):
        self.__data_nascimento = data_nascimento

    @nome_responsavel.setter
    def nome_responsavel(self, nome_responsavel: str):
        self.__nome_responsavel = nome_responsavel

    @cpf_responsavel.setter
    def cpf_responsavel(self, cpf_responsavel: str):
        self.__cpf_responsavel = cpf_responsavel

    def validar_cpf(self) -> bool:
        return len(self.cpf) == 11 and self.cpf.isdigit()

    def _calcular_idade(self) -> int:
        hoje = date.today()

        return (
            hoje.year
            - self.__data_nascimento.year
            - (
                (hoje.month, hoje.day)
                < (self.__data_nascimento.month, self.__data_nascimento.day)
            )
        )

    def verificar_idade(self) -> bool:
        return self._calcular_idade() < 18

    def verificar_responsavel(self) -> bool:
        if not self.verificar_idade():
            return True

        return (
            self.__nome_responsavel is not None
            and self.__cpf_responsavel is not None
        )
