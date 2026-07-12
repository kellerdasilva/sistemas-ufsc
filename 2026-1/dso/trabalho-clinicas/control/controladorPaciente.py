from model.paciente import Paciente
from Exceptions.pacienteException import PacienteException
from DAOs.paciente_dao import PacienteDAO
from datetime import date

class ControladorPaciente:
    def __init__(self):
        self.__paciente_dao = PacienteDAO()
        
    def cadastrar(self, nome, celular, cpf, data_nascimento, nome_responsavel=None, cpf_responsavel=None):
        if self.buscar_por_cpf(cpf) is not None:
            raise PacienteException(f"Já existe um paciente com o CPF {cpf}.")
        
        paciente = Paciente(nome, celular, cpf, data_nascimento)
        if not paciente.validar_cpf():
            raise PacienteException("CPF inválido.")
            
        if paciente.verificar_idade():
            if not nome_responsavel or not cpf_responsavel:
                raise PacienteException("Paciente menor de idade precisa de responsável.")
            paciente.nome_responsavel = nome_responsavel
            paciente.cpf_responsavel = cpf_responsavel
            
        self.__paciente_dao.add(paciente)
    
    def remover(self, cpf):
        paciente = self.buscar_por_cpf(cpf)
        if paciente is None:
            raise PacienteException(f"Paciente com CPF {cpf} não encontrado.")
        self.__paciente_dao.remove(cpf)
        
    def alterar(self, cpf, nome=None, celular=None, nome_responsavel=None, cpf_responsavel=None):
        paciente = self.buscar_por_cpf(cpf)
        if paciente is None:
            raise PacienteException(f"Paciente com CPF {cpf} não encontrado.")
            
        if nome:
            paciente.nome = nome
        if celular:
            paciente.celular = celular
        if nome_responsavel:
            paciente.nome_responsavel = nome_responsavel
        if cpf_responsavel:
            paciente.cpf_responsavel = cpf_responsavel
            
        # Atualiza o objeto no DAO para forçar a gravação no arquivo
        self.__paciente_dao.update(paciente)
    
    def listar(self):
        pacientes = self.__paciente_dao.get_all()
        if not pacientes:
            raise PacienteException("Nenhum paciente cadastrado.")
        
        return [
            {
                "nome": p.nome,
                "celular": p.celular,
                "cpf": p.cpf,
                "data_nascimento": p.data_nascimento,
                "nome_responsavel": p.nome_responsavel,
                "cpf_responsavel": p.cpf_responsavel
            }
            for p in pacientes
        ]
    
    def buscar_por_cpf(self, cpf):
        return self.__paciente_dao.get(cpf)
