import FreeSimpleGUI as sg

class TelaPrincipal:
    def __init__(
        self,
        tela_paciente,
        tela_clinica,
        tela_profissional,
        tela_tipo_atendimento,
        tela_atendimento,
        tela_procedimento,
        tela_pagamento,
        tela_relatorios,
    ):
        self.__tela_paciente = tela_paciente
        self.__tela_clinica = tela_clinica
        self.__tela_profissional = tela_profissional
        self.__tela_tipo_atendimento = tela_tipo_atendimento
        self.__tela_atendimento = tela_atendimento
        self.__tela_procedimento = tela_procedimento
        self.__tela_pagamento = tela_pagamento
        self.__tela_relatorios = tela_relatorios

    def mostrar_menu(self):
        sg.theme('LightBlue')
        layout = [
            [sg.Text('=== SISTEMA DE CLÍNICAS ===', font=('Helvetica', 16, 'bold'), justification='center', expand_x=True)],
            [sg.Frame('Cadastros', [
                [sg.Button('Pacientes', size=(15, 2)), sg.Button('Clínicas', size=(15, 2))],
                [sg.Button('Profissionais', size=(15, 2)), sg.Button('Tipos de atendimento', size=(15, 2))]
            ], expand_x=True, element_justification='c')],
            [sg.Frame('Registros', [
                [sg.Button('Atendimentos', size=(15, 2)), sg.Button('Procedimentos', size=(15, 2)), sg.Button('Pagamentos', size=(15, 2))]
            ], expand_x=True, element_justification='c')],
            [sg.Frame('Relatórios', [
                [sg.Button('Relatórios', size=(49, 2))]
            ], expand_x=True, element_justification='c')],
            [sg.Button('Sair', button_color=('white', 'red'), size=(10, 1))]
        ]

        window = sg.Window('Sistema de Clínicas', layout, element_justification='c')

        while True:
            event, values = window.read()

            if event == sg.WIN_CLOSED or event == 'Sair':
                break
            elif event == 'Pacientes':
                self.__tela_paciente.mostrar_menu()
            elif event == 'Clínicas':
                self.__tela_clinica.mostrar_menu()
            elif event == 'Profissionais':
                self.__tela_profissional.mostrar_menu()
            elif event == 'Tipos de atendimento':
                self.__tela_tipo_atendimento.mostrar_menu()
            elif event == 'Atendimentos':
                self.__tela_atendimento.mostrar_menu()
            elif event == 'Procedimentos':
                self.__tela_procedimento.mostrar_menu()
            elif event == 'Pagamentos':
                self.__tela_pagamento.mostrar_menu()
            elif event == 'Relatórios':
                self.__tela_relatorios.mostrar_menu()

        window.close()
