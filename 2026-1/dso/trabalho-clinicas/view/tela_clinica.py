import FreeSimpleGUI as sg
from Exceptions.clinicaException import ClinicaException
from Exceptions.profissionalException import ProfissionalException

class TelaClinica:
    def __init__(self, controlador_clinica):
        self.__controlador_clinica = controlador_clinica

    def mostrar_menu(self):
        layout = [
            [sg.Text('=== MENU CLÍNICA ===', font=('Helvetica', 14, 'bold'))],
            [sg.Button('Cadastrar clínica', key='1', size=(25, 1))],
            [sg.Button('Remover clínica', key='2', size=(25, 1))],
            [sg.Button('Alterar clínica', key='3', size=(25, 1))],
            [sg.Button('Listar clínicas', key='4', size=(25, 1))],
            [sg.Button('Vincular profissional', key='5', size=(25, 1))],
            [sg.Button('Desvincular profissional', key='6', size=(25, 1))],
            [sg.Button('Voltar', key='0', size=(10, 1), button_color=('white', 'gray'))]
        ]
        window = sg.Window('Menu Clínica', layout, modal=True, element_justification='c')
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
            elif event == '5':
                self.vincular_profissional()
            elif event == '6':
                self.desvincular_profissional()
        window.close()

    def cadastrar(self):
        layout = [
            [sg.Text('Nome da clínica:'), sg.InputText(key='nome')],
            [sg.Text('Cidade:'), sg.InputText(key='cidade')],
            [sg.Text('Horário de abertura (HH:MM):'), sg.InputText(key='abertura')],
            [sg.Text('Horário de fechamento (HH:MM):'), sg.InputText(key='fechamento')],
            [sg.Button('Cadastrar'), sg.Button('Cancelar', button_color=('white', 'gray'))]
        ]
        window = sg.Window('Cadastrar Clínica', layout, modal=True)
        event, values = window.read()
        if event == 'Cadastrar':
            try:
                self.__controlador_clinica.cadastrar(
                    values['nome'].strip(), 
                    values['cidade'].strip(), 
                    values['abertura'].strip(), 
                    values['fechamento'].strip()
                )
                sg.popup('Clínica cadastrada com sucesso!', title='Sucesso')
            except ClinicaException as e:
                sg.popup_error(f'Erro: {e}', title='Erro')
        window.close()

    def remover(self):
        layout = [
            [sg.Text('Nome da clínica a remover:'), sg.InputText(key='nome')],
            [sg.Text('Cidade:'), sg.InputText(key='cidade')],
            [sg.Button('Remover', button_color=('white', 'red')), sg.Button('Cancelar', button_color=('white', 'gray'))]
        ]
        window = sg.Window('Remover Clínica', layout, modal=True)
        event, values = window.read()
        if event == 'Remover':
            try:
                self.__controlador_clinica.remover(values['nome'].strip(), values['cidade'].strip())
                sg.popup('Clínica removida com sucesso!', title='Sucesso')
            except ClinicaException as e:
                sg.popup_error(f'Erro: {e}', title='Erro')
        window.close()

    def alterar(self):
        layout = [
            [sg.Text('Busca:', font=('Helvetica', 10, 'bold'))],
            [sg.Text('Nome atual:'), sg.InputText(key='nome')],
            [sg.Text('Cidade atual:'), sg.InputText(key='cidade')],
            [sg.Text('Novos dados (deixe em branco para manter):', font=('Helvetica', 10, 'bold'))],
            [sg.Text('Novo nome:'), sg.InputText(key='novo_nome')],
            [sg.Text('Nova cidade:'), sg.InputText(key='nova_cidade')],
            [sg.Text('Novo horário de abertura:'), sg.InputText(key='abertura')],
            [sg.Text('Novo horário de fechamento:'), sg.InputText(key='fechamento')],
            [sg.Button('Alterar'), sg.Button('Cancelar', button_color=('white', 'gray'))]
        ]
        window = sg.Window('Alterar Clínica', layout, modal=True)
        event, values = window.read()
        if event == 'Alterar':
            try:
                self.__controlador_clinica.alterar(
                    values['nome'].strip(), values['cidade'].strip(),
                    values['novo_nome'].strip() or None,
                    values['nova_cidade'].strip() or None,
                    values['abertura'].strip() or None,
                    values['fechamento'].strip() or None
                )
                sg.popup('Clínica alterada com sucesso!', title='Sucesso')
            except ClinicaException as e:
                sg.popup_error(f'Erro: {e}', title='Erro')
        window.close()

    def listar(self):
        try:
            clinicas = self.__controlador_clinica.listar()
            text = "=== CLÍNICAS ===\n\n"
            for i, c in enumerate(clinicas):
                profissionais = ", ".join(c['profissionais']) if c['profissionais'] else "nenhum vinculado"
                text += f"{i+1}. {c['nome']} | Cidade: {c['cidade']} | Funciona: {c['horario_abertura']} às {c['horario_fechamento']}\n" \
                        f"    Profissionais vinculados: {profissionais}\n"
            sg.popup_scrolled(text, title='Listar Clínicas', size=(70, 15))
        except ClinicaException as e:
            sg.popup_error(f'Erro: {e}', title='Erro')

    def vincular_profissional(self):
        layout = [
            [sg.Text('Nome da clínica:'), sg.InputText(key='nome')],
            [sg.Text('Cidade:'), sg.InputText(key='cidade')],
            [sg.Text('CPF do profissional a vincular:'), sg.InputText(key='cpf')],
            [sg.Button('Vincular'), sg.Button('Cancelar', button_color=('white', 'gray'))]
        ]
        window = sg.Window('Vincular Profissional à Clínica', layout, modal=True)
        event, values = window.read()
        if event == 'Vincular':
            try:
                self.__controlador_clinica.vincular_profissional(
                    values['nome'].strip(), values['cidade'].strip(), values['cpf'].strip()
                )
                sg.popup('Profissional vinculado à clínica com sucesso!', title='Sucesso')
            except (ClinicaException, ProfissionalException) as e:
                sg.popup_error(f'Erro: {e}', title='Erro')
        window.close()

    def desvincular_profissional(self):
        layout = [
            [sg.Text('Nome da clínica:'), sg.InputText(key='nome')],
            [sg.Text('Cidade:'), sg.InputText(key='cidade')],
            [sg.Text('CPF do profissional a desvincular:'), sg.InputText(key='cpf')],
            [sg.Button('Desvincular', button_color=('white', 'red')), sg.Button('Cancelar', button_color=('white', 'gray'))]
        ]
        window = sg.Window('Desvincular Profissional da Clínica', layout, modal=True)
        event, values = window.read()
        if event == 'Desvincular':
            try:
                self.__controlador_clinica.desvincular_profissional(
                    values['nome'].strip(), values['cidade'].strip(), values['cpf'].strip()
                )
                sg.popup('Profissional desvinculado da clínica com sucesso!', title='Sucesso')
            except (ClinicaException, ProfissionalException) as e:
                sg.popup_error(f'Erro: {e}', title='Erro')
        window.close()
