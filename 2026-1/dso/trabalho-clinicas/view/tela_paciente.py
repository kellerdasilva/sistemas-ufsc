import FreeSimpleGUI as sg
from datetime import date
from Exceptions.pacienteException import PacienteException

class TelaPaciente:
    def __init__(self, controlador_paciente):
        self.__controlador_paciente = controlador_paciente

    def mostrar_menu(self):
        layout = [
            [sg.Text('=== MENU PACIENTE ===', font=('Helvetica', 14, 'bold'))],
            [sg.Button('Cadastrar paciente', key='1', size=(20, 1))],
            [sg.Button('Remover paciente', key='2', size=(20, 1))],
            [sg.Button('Alterar paciente', key='3', size=(20, 1))],
            [sg.Button('Listar pacientes', key='4', size=(20, 1))],
            [sg.Button('Voltar', key='0', size=(10, 1), button_color=('white', 'gray'))]
        ]
        window = sg.Window('Menu Paciente', layout, modal=True, element_justification='c')
        while True:
            event, values = window.read()
            if event == sg.WIN_CLOSED or event == '0':
                break
            elif event == '1':
                self.cadastrar()
            elif event == '2':
                self.remover()
            elif event == '3':
                self.alterar()
            elif event == '4':
                self.listar()
        window.close()

    def cadastrar(self):
        layout = [
            [sg.Text('Nome:'), sg.InputText(key='nome')],
            [sg.Text('Celular:'), sg.InputText(key='celular')],
            [sg.Text('CPF (somente números):'), sg.InputText(key='cpf')],
            [sg.Text('Data de nascimento (DD/MM/AAAA):'), sg.InputText(key='data_str')],
            [sg.Text('Se o paciente for menor de idade, preencha também:', font=('Helvetica', 9, 'italic'))],
            [sg.Text('Nome do responsável:'), sg.InputText(key='nome_resp')],
            [sg.Text('CPF do responsável:'), sg.InputText(key='cpf_resp')],
            [sg.Button('Cadastrar'), sg.Button('Cancelar', button_color=('white', 'gray'))]
        ]
        window = sg.Window('Cadastrar Paciente', layout, modal=True)
        event, values = window.read()

        if event == 'Cadastrar':
            try:
                nome = values['nome'].strip()
                celular = values['celular'].strip()
                cpf = values['cpf'].strip()
                data_str = values['data_str'].strip()
                data_nascimento = date(*reversed([int(x) for x in data_str.split("/")]))
                nome_responsavel = values['nome_resp'].strip() or None
                cpf_responsavel = values['cpf_resp'].strip() or None

                self.__controlador_paciente.cadastrar(
                    nome, celular, cpf, data_nascimento, nome_responsavel, cpf_responsavel
                )
                sg.popup('Paciente cadastrado com sucesso!', title='Sucesso')
            except PacienteException as e:
                sg.popup_error(f'Erro: {e}', title='Erro')
            except Exception as e:
                sg.popup_error(f'Erro: {e}', title='Erro')
        window.close()

    def remover(self):
        layout = [
            [sg.Text('CPF do paciente a remover:'), sg.InputText(key='cpf')],
            [sg.Button('Remover', button_color=('white', 'red')), sg.Button('Cancelar', button_color=('white', 'gray'))]
        ]
        window = sg.Window('Remover Paciente', layout, modal=True)
        event, values = window.read()
        if event == 'Remover':
            try:
                self.__controlador_paciente.remover(values['cpf'].strip())
                sg.popup('Paciente removido com sucesso!', title='Sucesso')
            except PacienteException as e:
                sg.popup_error(f'Erro: {e}', title='Erro')
        window.close()

    def alterar(self):
        layout = [
            [sg.Text('CPF do paciente a alterar:'), sg.InputText(key='cpf')],
            [sg.Text('Novos dados (deixe em branco para manter):', font=('Helvetica', 10, 'bold'))],
            [sg.Text('Novo nome:'), sg.InputText(key='nome')],
            [sg.Text('Novo celular:'), sg.InputText(key='celular')],
            [sg.Text('Novo nome do responsável:'), sg.InputText(key='nome_resp')],
            [sg.Text('Novo CPF do responsável:'), sg.InputText(key='cpf_resp')],
            [sg.Button('Alterar'), sg.Button('Cancelar', button_color=('white', 'gray'))]
        ]
        window = sg.Window('Alterar Paciente', layout, modal=True)
        event, values = window.read()
        if event == 'Alterar':
            try:
                self.__controlador_paciente.alterar(
                    values['cpf'].strip(),
                    values['nome'].strip() or None,
                    values['celular'].strip() or None,
                    values['nome_resp'].strip() or None,
                    values['cpf_resp'].strip() or None
                )
                sg.popup('Paciente alterado com sucesso!', title='Sucesso')
            except PacienteException as e:
                sg.popup_error(f'Erro: {e}', title='Erro')
        window.close()

    def listar(self):
        try:
            pacientes = self.__controlador_paciente.listar()
            text = "=== PACIENTES ===\n\n"
            for i, p in enumerate(pacientes):
                text += f"{i+1}. {p['nome']} | CPF: {p['cpf']} | Celular: {p['celular']} | Nascimento: {p['data_nascimento']}\n"
            sg.popup_scrolled(text, title='Listar Pacientes', size=(60, 15))
        except PacienteException as e:
            sg.popup_error(f'Erro: {e}', title='Erro')
