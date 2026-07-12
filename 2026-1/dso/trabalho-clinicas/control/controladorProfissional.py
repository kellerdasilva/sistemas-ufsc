from model.profissional import Profissional
from Exceptions.profissionalException import ProfissionalException
from DAOs.profissional_dao import ProfissionalDAO

class ControladorProfissional:
    def __init__(self):
        self.__profissional_dao = ProfissionalDAO()

    def cadastrar(self, nome, celular, cpf, especialidade, registro_profissional):
        if self.buscar_por_cpf(cpf) is not None:
            raise ProfissionalException(f"Já existe um profissional com o CPF {cpf}.")
        
        profissional = Profissional(nome, celular, cpf, especialidade, registro_profissional)
        
        if not profissional.validar_cpf():
            raise ProfissionalException("CPF inválido.")
        if not profissional.validar_registro():
            raise ProfissionalException("Registro profissional inválido.")
            
        self.__profissional_dao.add(profissional)

    def remover(self, cpf):
        profissional = self.buscar_por_cpf(cpf)
        if profissional is None:
            raise ProfissionalException(f"Profissional com CPF {cpf} não encontrado.")
        self.__profissional_dao.remove(cpf)

    def alterar(self, cpf, nome=None, celular=None, especialidade=None, registro_profissional=None):
        profissional = self.buscar_por_cpf(cpf)
        if profissional is None:
            raise ProfissionalException(f"Profissional com CPF {cpf} não encontrado.")
            
        if nome:
            profissional.nome = nome
        if celular:
            profissional.celular = celular
        if especialidade:
            profissional.especialidade = especialidade
        if registro_profissional:
            profissional.registro_profissional = registro_profissional
            
        self.__profissional_dao.update(profissional)

    def listar(self):
        profissionais = self.__profissional_dao.get_all()
        if not profissionais:
            raise ProfissionalException("Nenhum profissional cadastrado.")
        
        return [
            {
                "nome": p.nome,
                "celular": p.celular,
                "cpf": p.cpf,
                "especialidade": p.especialidade,
                "registro_profissional": p.registro_profissional
            }
            for p in profissionais
        ]

    def buscar_por_cpf(self, cpf):
        return self.__profissional_dao.get(cpf)
