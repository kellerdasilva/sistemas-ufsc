from model.atendimento import Atendimento
from Exceptions.atendimentoException import AtendimentoException
from DAOs.atendimento_dao import AtendimentoDAO

class ControladorAtendimento:
    def __init__(self, controlador_paciente, controlador_clinica, controlador_profissional, controlador_tipo_atendimento):
        self.__atendimento_dao = AtendimentoDAO()
        self.__controlador_paciente = controlador_paciente
        self.__controlador_clinica = controlador_clinica
        self.__controlador_profissional = controlador_profissional
        self.__controlador_tipo_atendimento = controlador_tipo_atendimento

    def _gerar_chave(self, data, horario_inicio, cpf_paciente):
        return f"{cpf_paciente}_{data}_{horario_inicio}"

    def _obter_chave_por_index(self, index):
        atendimentos = list(self.__atendimento_dao.get_all())
        if index < 0 or index >= len(atendimentos):
            raise AtendimentoException("Atendimento não encontrado.")
        a = atendimentos[index]
        return self._gerar_chave(a.data, a.horario_inicio, a.paciente.cpf)

    def get_todos_atendimentos(self):
        return list(self.__atendimento_dao.get_all())

    def cadastrar(self, data, horario_inicio, horario_fim, valor, nome_clinica, cidade_clinica, cpf_paciente, cpf_profissional, nome_tipo):
        clinica = self.__controlador_clinica.buscar(nome_clinica, cidade_clinica)
        if clinica is None: raise AtendimentoException("Clínica não encontrada.")
        
        paciente = self.__controlador_paciente.buscar_por_cpf(cpf_paciente)
        if paciente is None: raise AtendimentoException("Paciente não encontrado.")
        
        profissional = self.__controlador_profissional.buscar_por_cpf(cpf_profissional)
        if profissional is None: raise AtendimentoException("Profissional não encontrado.")
        
        tipo = self.__controlador_tipo_atendimento.buscar(nome_tipo)
        if tipo is None: raise AtendimentoException("Tipo de atendimento não encontrado.")

        if not clinica.validar_horario_atendimento(horario_inicio, horario_fim):
            raise AtendimentoException("Horário fora do funcionamento da clínica.")
        if paciente.verificar_idade() and not paciente.verificar_responsavel():
            raise AtendimentoException("Paciente menor de idade sem responsável cadastrado.")

        chave = self._gerar_chave(data, horario_inicio, cpf_paciente)
        if self.__atendimento_dao.get(chave) is not None:
            raise AtendimentoException("Já existe um atendimento para este paciente neste horário.")

        atendimento = Atendimento(data, horario_inicio, horario_fim, valor, clinica, paciente, profissional, tipo)
        self.__atendimento_dao.add(chave, atendimento)
        return atendimento

    def remover(self, index):
        chave = self._obter_chave_por_index(index)
        self.__atendimento_dao.remove(chave)

    def alterar(self, index, data=None, horario_inicio=None, horario_fim=None, valor=None):
        chave_antiga = self._obter_chave_por_index(index)
        atendimento = self.__atendimento_dao.get(chave_antiga)
        
        novo_data = data if data else atendimento.data
        novo_horario = horario_inicio if horario_inicio else atendimento.horario_inicio
        chave_nova = self._gerar_chave(novo_data, novo_horario, atendimento.paciente.cpf)
        
        mudou_chave = (chave_antiga != chave_nova)
        if mudou_chave:
            if self.__atendimento_dao.get(chave_nova) is not None:
                raise AtendimentoException("Já existe um atendimento para este paciente neste novo horário.")
            self.__atendimento_dao.remove(chave_antiga)
        
        if data: atendimento.data = data
        if horario_inicio: atendimento.horario_inicio = horario_inicio
        if horario_fim: atendimento.horario_fim = horario_fim
        if valor is not None: atendimento.valor = valor

        if mudou_chave:
            self.__atendimento_dao.add(chave_nova, atendimento)
        else:
            self.__atendimento_dao.update(chave_antiga, atendimento)

    def listar(self):
        atendimentos = list(self.__atendimento_dao.get_all())
        if not atendimentos:
            raise AtendimentoException("Nenhum atendimento registrado.")
        
        return [
            {
                "status": a.status,
                "data": a.data,
                "horario_inicio": a.horario_inicio,
                "horario_fim": a.horario_fim,
                "tipo_atendimento": a.tipo_atendimento.nome,
                "paciente": a.paciente.nome,
                "profissional": a.profissional.nome,
                "clinica": a.clinica.nome,
                "valor_total": a.calcular_valor_total(),
                "valor_restante": a.calcular_valor_restante()
            }
            for a in atendimentos
        ]

    def buscar(self, index):
        chave = self._obter_chave_por_index(index)
        return self.__atendimento_dao.get(chave)

    def cancelar(self, index):
        chave = self._obter_chave_por_index(index)
        atendimento = self.__atendimento_dao.get(chave)
        atendimento.cancelar()
        self.__atendimento_dao.update(chave, atendimento)

    def reagendar(self, index):
        chave = self._obter_chave_por_index(index)
        atendimento = self.__atendimento_dao.get(chave)
        atendimento.agendar()
        self.__atendimento_dao.update(chave, atendimento)

    def atualizar_atendimento(self, atendimento):
        # Utilizado pelos controladores de Procedimento e Pagamento para persistir mudanças na raiz de agregação
        chave = self._gerar_chave(atendimento.data, atendimento.horario_inicio, atendimento.paciente.cpf)
        self.__atendimento_dao.update(chave, atendimento)

    def relatorio_clinicas_mais_atendimentos(self):
        atendimentos = list(self.__atendimento_dao.get_all())
        if not atendimentos:
            raise AtendimentoException("Nenhum atendimento registrado.")
        contagem = {}
        for a in atendimentos:
            chave = f"{a.clinica.nome} - {a.clinica.cidade}"
            contagem[chave] = contagem.get(chave, 0) + 1
        return sorted(contagem.items(), key=lambda x: x[1], reverse=True)

    def relatorio_atendimentos_mais_caros_baratos(self):
        atendimentos = list(self.__atendimento_dao.get_all())
        if not atendimentos:
            raise AtendimentoException("Nenhum atendimento registrado.")
        ordenados = sorted(atendimentos, key=lambda a: a.calcular_valor_total(), reverse=True)
        mais_caros = [
            {"data": a.data, "paciente": a.paciente.nome, "valor_total": a.calcular_valor_total()} for a in ordenados[:3]
        ]
        mais_baratos = [
            {"data": a.data, "paciente": a.paciente.nome, "valor_total": a.calcular_valor_total()} for a in ordenados[-3:]
        ]
        return {
            "mais_caros": mais_caros,
            "mais_baratos": mais_baratos
        }
