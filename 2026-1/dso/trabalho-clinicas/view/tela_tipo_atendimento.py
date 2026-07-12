import FreeSimpleGUI as sg
from Exceptions.tipoAtendimentoException import TipoAtendimentoException

class TelaTipoAtendimento:
    def __init__(self, controlador_tipo_atendimento):
        self.__controlador_tipo_atendimento = controlador_tipo_atendimento

    def mostrar_menu(self):
        layout = [
            [sg.Text('=== MENU TIPO DE ATENDIMENTO ===', font=('Helvetica', 14, 'bold'))],
            [sg.Button('Cadastrar tipo', key='1', size=(25, 1))],
            [sg.Button('Remover tipo', key='2', size=(25, 1))],
            [sg.Button('Alterar tipo', key='3', size=(25, 1))],
            [sg.Button('Listar tipos', key='4', size=(25, 1))],
            [sg.Button('Voltar', key='0', size=(10, 1), button_color=('white', 'gray'))]
        ]
        window = sg.Window('Menu Tipo de Atendimento', layout, modal=True, element_justification='c')
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
            [sg.Text('Nome do tipo:'), sg.InputText(key='nome')],
            [sg.Text('Descrição:'), sg.InputText(key='descricao')],
            [sg.Text('Valor base (R$):'), sg.InputText(key='valor_base')],
            [sg.Button('Cadastrar'), sg.Button('Cancelar', button_color=('white', 'gray'))]
        ]
        window = sg.Window('Cadastrar Tipo de Atendimento', layout, modal=True)
        event, values = window.read()
        
        if event == 'Cadastrar':
            try:
                nome = values['nome'].strip()
                descricao = values['descricao'].strip()
                valor_base = float(values['valor_base'].strip())
                
                self.__controlador_tipo_atendimento.cadastrar(nome, descricao, valor_base)
                sg.popup('Tipo de atendimento cadastrado com sucesso!', title='Sucesso')
            except TipoAtendimentoException as e:
                sg.popup_error(f'Erro: {e}', title='Erro')
            except ValueError:
                sg.popup_error('Erro: Valor base deve ser um número válido.', title='Erro')
        window.close()

    def remover(self):
        layout = [
            [sg.Text('Nome do tipo a remover:'), sg.InputText(key='nome')],
            [sg.Button('Remover', button_color=('white', 'red')), sg.Button('Cancelar', button_color=('white', 'gray'))]
        ]
        window = sg.Window('Remover Tipo de Atendimento', layout, modal=True)
        event, values = window.read()
        if event == 'Remover':
            try:
                self.__controlador_tipo_atendimento.remover(values['nome'].strip())
                sg.popup('Tipo de atendimento removido com sucesso!', title='Sucesso')
            except TipoAtendimentoException as e:
                sg.popup_error(f'Erro: {e}', title='Erro')
        window.close()

    def alterar(self):
        layout = [
            [sg.Text('Nome do tipo a alterar:'), sg.InputText(key='nome')],
            [sg.Text('Novos dados (deixe em branco para manter):', font=('Helvetica', 10, 'bold'))],
            [sg.Text('Novo nome:'), sg.InputText(key='novo_nome')],
            [sg.Text('Nova descrição:'), sg.InputText(key='descricao')],
            [sg.Text('Novo valor base (R$):'), sg.InputText(key='valor_base')],
            [sg.Button('Alterar'), sg.Button('Cancelar', button_color=('white', 'gray'))]
        ]
        window = sg.Window('Alterar Tipo de Atendimento', layout, modal=True)
        event, values = window.read()
        if event == 'Alterar':
            try:
                nome = values['nome'].strip()
                novo_nome = values['novo_nome'].strip() or None
                descricao = values['descricao'].strip() or None
                valor_str = values['valor_base'].strip()
                valor_base = float(valor_str) if valor_str else None
                
                self.__controlador_tipo_atendimento.alterar(nome, novo_nome, descricao, valor_base)
                sg.popup('Tipo de atendimento alterado com sucesso!', title='Sucesso')
            except TipoAtendimentoException as e:
                sg.popup_error(f'Erro: {e}', title='Erro')
            except ValueError:
                sg.popup_error('Erro: Valor base deve ser um número válido.', title='Erro')
        window.close()

    def listar(self):
        try:
            tipos = self.__controlador_tipo_atendimento.listar()
            text = "=== TIPOS DE ATENDIMENTO ===\n\n"
            for i, t in enumerate(tipos):
                text += f"{i+1}. {t['nome']} | Descrição: {t['descricao']} | Valor base: R${t['valor_base']:.2f}\n"
            sg.popup_scrolled(text, title='Listar Tipos de Atendimento', size=(60, 15))
        except TipoAtendimentoException as e:
            sg.popup_error(f'Erro: {e}', title='Erro')