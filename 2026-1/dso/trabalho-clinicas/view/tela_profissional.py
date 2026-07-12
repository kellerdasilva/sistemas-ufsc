import FreeSimpleGUI as sg
from Exceptions.profissionalException import ProfissionalException

class TelaProfissional:
    def __init__(self, controlador_profissional):
        self.__controlador_profissional = controlador_profissional

    def mostrar_menu(self):
        layout = [
            [sg.Text('=== MENU PROFISSIONAL ===', font=('Helvetica', 14, 'bold'))],
            [sg.Button('Cadastrar profissional', key='1', size=(25, 1))],
            [sg.Button('Remover profissional', key='2', size=(25, 1))],
            [sg.Button('Alterar profissional', key='3', size=(25, 1))],
            [sg.Button('Listar profissionais', key='4', size=(25, 1))],
            [sg.Button('Voltar', key='0', size=(10, 1), button_color=('white', 'gray'))]
        ]
        window = sg.Window('Menu Profissional', layout, modal=True, element_justification='c')
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
            [sg.Text('Especialidade:'), sg.InputText(key='especialidade')],
            [sg.Text('Registro profissional:'), sg.InputText(key='registro')],
            [sg.Button('Cadastrar'), sg.Button('Cancelar', button_color=('white', 'gray'))]
        ]
        window = sg.Window('Cadastrar Profissional', layout, modal=True)
        event, values = window.read()
        
        if event == 'Cadastrar':
            try:
                nome = values['nome'].strip()
                celular = values['celular'].strip()
                cpf = values['cpf'].strip()
                especialidade = values['especialidade'].strip()
                registro = values['registro'].strip()
                
                self.__controlador_profissional.cadastrar(nome, celular, cpf, especialidade, registro)
                sg.popup('Profissional cadastrado com sucesso!', title='Sucesso')
            except ProfissionalException as e:
                sg.popup_error(f'Erro: {e}', title='Erro')
            except Exception as e:
                sg.popup_error(f'Erro: {e}', title='Erro')
        window.close()

    def remover(self):
        layout = [
            [sg.Text('CPF do profissional a remover:'), sg.InputText(key='cpf')],
            [sg.Button('Remover', button_color=('white', 'red')), sg.Button('Cancelar', button_color=('white', 'gray'))]
        ]
        window = sg.Window('Remover Profissional', layout, modal=True)
        event, values = window.read()
        if event == 'Remover':
            try:
                self.__controlador_profissional.remover(values['cpf'].strip())
                sg.popup('Profissional removido com sucesso!', title='Sucesso')
            except ProfissionalException as e:
                sg.popup_error(f'Erro: {e}', title='Erro')
        window.close()

    def alterar(self):
        layout = [
            [sg.Text('CPF do profissional a alterar:'), sg.InputText(key='cpf')],
            [sg.Text('Novos dados (deixe em branco para manter):', font=('Helvetica', 10, 'bold'))],
            [sg.Text('Novo nome:'), sg.InputText(key='nome')],
            [sg.Text('Novo celular:'), sg.InputText(key='celular')],
            [sg.Text('Nova especialidade:'), sg.InputText(key='especialidade')],
            [sg.Text('Novo registro profissional:'), sg.InputText(key='registro')],
            [sg.Button('Alterar'), sg.Button('Cancelar', button_color=('white', 'gray'))]
        ]
        window = sg.Window('Alterar Profissional', layout, modal=True)
        event, values = window.read()
        if event == 'Alterar':
            try:
                self.__controlador_profissional.alterar(
                    values['cpf'].strip(),
                    values['nome'].strip() or None,
                    values['celular'].strip() or None,
                    values['especialidade'].strip() or None,
                    values['registro'].strip() or None
                )
                sg.popup('Profissional alterado com sucesso!', title='Sucesso')
            except ProfissionalException as e:
                sg.popup_error(f'Erro: {e}', title='Erro')
        window.close()

    def listar(self):
        try:
            profissionais = self.__controlador_profissional.listar()
            text = "=== PROFISSIONAIS ===\n\n"
            for i, p in enumerate(profissionais):
                text += f"{i+1}. {p['nome']} | CPF: {p['cpf']} | Especialidade: {p['especialidade']} | Registro: {p['registro_profissional']}\n"
            sg.popup_scrolled(text, title='Listar Profissionais', size=(60, 15))
        except ProfissionalException as e:
            sg.popup_error(f'Erro: {e}', title='Erro')
