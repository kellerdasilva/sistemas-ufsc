from model.clinica import Clinica
from Exceptions.clinicaException import ClinicaException
from DAOs.clinica_dao import ClinicaDAO

class ControladorClinica:
    def __init__(self, controlador_profissional):
        self.__clinica_dao = ClinicaDAO()
        self.__controlador_profissional = controlador_profissional

    def cadastrar(self, nome, cidade, horario_abertura, horario_fechamento):
        if self.buscar(nome, cidade) is not None:
            raise ClinicaException(f"Já existe uma clínica com o nome '{nome}' em {cidade}.")
        
        clinica = Clinica(nome, cidade, horario_abertura, horario_fechamento)
        self.__clinica_dao.add(clinica)

    def remover(self, nome, cidade):
        clinica = self.buscar(nome, cidade)
        if clinica is None:
            raise ClinicaException(f"Clínica '{nome}' em {cidade} não encontrada.")
        self.__clinica_dao.remove(nome, cidade)

    def alterar(self, nome, cidade, novo_nome=None, nova_cidade=None, horario_abertura=None, horario_fechamento=None):
        clinica = self.buscar(nome, cidade)
        if clinica is None:
            raise ClinicaException(f"Clínica '{nome}' em {cidade} não encontrada.")
        
        mudou_chave = (novo_nome is not None and novo_nome != nome) or (nova_cidade is not None and nova_cidade != cidade)
        
        if mudou_chave:
            self.__clinica_dao.remove(nome, cidade)
            
        if novo_nome:
            clinica.nome = novo_nome
        if nova_cidade:
            clinica.cidade = nova_cidade
        if horario_abertura:
            clinica.horario_abertura = horario_abertura
        if horario_fechamento:
            clinica.horario_fechamento = horario_fechamento
            
        if mudou_chave:
            self.__clinica_dao.add(clinica)
        else:
            self.__clinica_dao.update(clinica)

    def listar(self):
        clinicas = self.__clinica_dao.get_all()
        if not clinicas:
            raise ClinicaException("Nenhuma clínica cadastrada.")
        
        return [
            {
                "nome": c.nome,
                "cidade": c.cidade,
                "horario_abertura": c.horario_abertura,
                "horario_fechamento": c.horario_fechamento,
                "profissionais": [p.nome for p in c.profissionais]
            }
            for c in clinicas
        ]

    def buscar(self, nome, cidade):
        return self.__clinica_dao.get(nome, cidade)

    def vincular_profissional(self, nome, cidade, cpf_profissional):
        clinica = self.buscar(nome, cidade)
        if clinica is None:
            raise ClinicaException(f"Clínica '{nome}' em {cidade} não encontrada.")
            
        profissional = self.__controlador_profissional.buscar_por_cpf(cpf_profissional)
        if profissional is None:
            raise ClinicaException(f"Profissional com CPF {cpf_profissional} não encontrado.")
            
        clinica.adicionar_profissional(profissional)
        self.__clinica_dao.update(clinica)

    def desvincular_profissional(self, nome, cidade, cpf_profissional):
        clinica = self.buscar(nome, cidade)
        if clinica is None:
            raise ClinicaException(f"Clínica '{nome}' em {cidade} não encontrada.")
            
        profissional = self.__controlador_profissional.buscar_por_cpf(cpf_profissional)
        if profissional is None:
            raise ClinicaException(f"Profissional com CPF {cpf_profissional} não encontrado.")
            
        clinica.remover_profissional(profissional)
        self.__clinica_dao.update(clinica)
