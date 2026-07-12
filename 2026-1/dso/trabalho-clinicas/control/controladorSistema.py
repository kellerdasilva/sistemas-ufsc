from control.controladorPaciente import ControladorPaciente
from control.controladorClinica import ControladorClinica
from control.controladorProfissional import ControladorProfissional
from control.controladorTipoAtendimento import ControladorTipoAtendimento
from control.controladorAtendimento import ControladorAtendimento
from control.controladorProcedimento import ControladorProcedimento
from control.controladorPagamento import ControladorPagamento

from view.tela_paciente import TelaPaciente
from view.tela_clinica import TelaClinica
from view.tela_profissional import TelaProfissional
from view.tela_tipo_atendimento import TelaTipoAtendimento
from view.tela_atendimento import TelaAtendimento
from view.tela_procedimento import TelaProcedimento
from view.tela_pagamento import TelaPagamento
from view.tela_relatorios import TelaRelatorios
from view.tela_principal import TelaPrincipal

class ControladorSistema:
    def __init__(self):
        # Controladores
        self.__controlador_paciente = ControladorPaciente()
        self.__controlador_profissional = ControladorProfissional()
        self.__controlador_clinica = ControladorClinica(self.__controlador_profissional)
        self.__controlador_tipo_atendimento = ControladorTipoAtendimento()
        self.__controlador_atendimento = ControladorAtendimento(
            self.__controlador_paciente,
            self.__controlador_clinica,
            self.__controlador_profissional,
            self.__controlador_tipo_atendimento,
        )
        self.__controlador_procedimento = ControladorProcedimento(
            self.__controlador_profissional,
            self.__controlador_atendimento,
        )
        self.__controlador_pagamento = ControladorPagamento(
            self.__controlador_atendimento,
        )

        # Telas
        self.__tela_paciente = TelaPaciente(self.__controlador_paciente)
        self.__tela_clinica = TelaClinica(self.__controlador_clinica)
        self.__tela_profissional = TelaProfissional(self.__controlador_profissional)
        self.__tela_tipo_atendimento = TelaTipoAtendimento(self.__controlador_tipo_atendimento)
        self.__tela_atendimento = TelaAtendimento(self.__controlador_atendimento)
        self.__tela_procedimento = TelaProcedimento(self.__controlador_procedimento)
        self.__tela_pagamento = TelaPagamento(self.__controlador_pagamento)
        self.__tela_relatorios = TelaRelatorios(
            self.__controlador_atendimento,
            self.__controlador_procedimento,
        )
        self.__tela_principal = TelaPrincipal(
            self.__tela_paciente,
            self.__tela_clinica,
            self.__tela_profissional,
            self.__tela_tipo_atendimento,
            self.__tela_atendimento,
            self.__tela_procedimento,
            self.__tela_pagamento,
            self.__tela_relatorios,
        )

    def iniciar(self):
        self.__tela_principal.mostrar_menu()
