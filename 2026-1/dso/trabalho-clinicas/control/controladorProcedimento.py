from model.procedimento import Procedimento
from Exceptions.procedimentoException import ProcedimentoException

class ControladorProcedimento:
    def __init__(self, controlador_profissional, controlador_atendimento):
        self.__controlador_profissional = controlador_profissional
        self.__controlador_atendimento = controlador_atendimento

    def _obter_todos_procedimentos(self):
        # Reconstrói a lista iterando sobre todos os atendimentos do DAO
        registros = []
        for atendimento in self.__controlador_atendimento.get_todos_atendimentos():
            for proc in atendimento.procedimentos:
                registros.append((proc, atendimento))
        return registros

    def cadastrar(self, descricao, custo, cpf_profissional, index_atendimento):
        profissional = self.__controlador_profissional.buscar_por_cpf(cpf_profissional)
        if profissional is None:
            raise ProcedimentoException("Profissional não encontrado.")
            
        atendimento = self.__controlador_atendimento.buscar(index_atendimento)
        if atendimento.esta_cancelado():
            raise ProcedimentoException("Não é possível registrar procedimento em um atendimento cancelado.")
            
        procedimento = Procedimento(descricao, custo, profissional)
        atendimento.adicionar_procedimento(procedimento)
        
        # Persiste o estado atualizado do Atendimento no arquivo
        self.__controlador_atendimento.atualizar_atendimento(atendimento)
        return procedimento

    def remover(self, index):
        registros = self._obter_todos_procedimentos()
        if index < 0 or index >= len(registros):
            raise ProcedimentoException(f"Índice de procedimento inválido: {index}")
            
        procedimento, atendimento = registros[index]
        atendimento.remover_procedimento(procedimento)
        self.__controlador_atendimento.atualizar_atendimento(atendimento)

    def alterar(self, index, descricao=None, custo=None, cpf_profissional=None):
        registros = self._obter_todos_procedimentos()
        if index < 0 or index >= len(registros):
            raise ProcedimentoException(f"Índice de procedimento inválido: {index}")
            
        procedimento, atendimento = registros[index]
        
        if descricao:
            procedimento.descricao = descricao
        if custo is not None:
            if custo < 0:
                raise ProcedimentoException("Custo inválido")
            procedimento.custo = custo
        if cpf_profissional:
            profissional = self.__controlador_profissional.buscar_por_cpf(cpf_profissional)
            if profissional is None: 
                raise ProcedimentoException("Profissional não encontrado.")
            procedimento.profissional_responsavel = profissional
            
        self.__controlador_atendimento.atualizar_atendimento(atendimento)

    def listar(self):
        registros = self._obter_todos_procedimentos()
        if not registros:
            raise ProcedimentoException("Nenhum procedimento registrado.")

        return [
            {
                "descricao": p.descricao,
                "custo": p.calcular_custo(),
                "profissional": p.profissional_responsavel.nome
            }
            for p, _ in registros
        ]

    def buscar(self, index):
        registros = self._obter_todos_procedimentos()
        if index < 0 or index >= len(registros):
            raise ProcedimentoException(f"Índice de procedimento inválido: {index}")
        return registros[index][0]

    def relatorio_mais_populares(self):
        registros = self._obter_todos_procedimentos()
        if not registros:
            raise ProcedimentoException("Nenhum procedimento registrado.")
        contagem = {}
        for p, _ in registros:
            contagem[p.descricao] = contagem.get(p.descricao, 0) + 1
        return sorted(contagem.items(), key=lambda x: x[1], reverse=True)

    def relatorio_mais_caros_baratos(self):
        registros = self._obter_todos_procedimentos()
        if not registros:
            raise ProcedimentoException("Nenhum procedimento registrado.")
        ordenados = sorted((p for p, _ in registros), key=lambda p: p.calcular_custo(), reverse=True)
        mais_caros = [
            {"descricao": p.descricao, "custo": p.calcular_custo()} for p in ordenados[:3]
        ]
        mais_baratos = [
            {"descricao": p.descricao, "custo": p.calcular_custo()} for p in ordenados[-3:]
        ]
        return {
            "mais_caros": mais_caros,
            "mais_baratos": mais_baratos
        }
