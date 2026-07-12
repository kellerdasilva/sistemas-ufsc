from model.pessoa import Pessoa

class Profissional(Pessoa):
    def __init__(
        self,
        nome: str,
        celular: str,
        cpf: str,
        especialidade: str,
        registro_profissional: str,
    ):
        super().__init__(nome, celular, cpf)
        self.__especialidade = especialidade
        self.__registro_profissional = registro_profissional

    @property
    def especialidade(self) -> str:
        return self.__especialidade

    @property
    def registro_profissional(self) -> str:
        return self.__registro_profissional

    @especialidade.setter
    def especialidade(self, especialidade: str):
        self.__especialidade = especialidade

    @registro_profissional.setter
    def registro_profissional(self, registro_profissional: str):
        self.__registro_profissional = registro_profissional

    def validar_cpf(self) -> bool:
        return len(self.cpf) == 11 and self.cpf.isdigit()

    def validar_registro(self) -> bool:
        return bool(self.__registro_profissional.strip())
