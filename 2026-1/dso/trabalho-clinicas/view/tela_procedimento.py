import FreeSimpleGUI as sg
from Exceptions.procedimentoException import ProcedimentoException

class TelaProcedimento:
    def __init__(self, controlador_procedimento):
        self.__controlador_procedimento = controlador_procedimento

    def mostrar_menu(self):
        layout = [
            [sg.Text('=== MENU PROCEDIMENTO ===', font=('Helvetica', 14, 'bold'))],
            [sg.Button('Registrar procedimento', key='1', size=(25, 1))],
            [sg.Button('Remover procedimento', key='2', size=(25, 1))],
            [sg.Button('Alterar procedimento', key='3', size=(25, 1))],
            [sg.Button('Listar procedimentos', key='4', size=(25, 1))],
            [sg.Button('Voltar', key='0', size=(10, 1), button_color=('white', 'gray'))]
        ]
        window = sg.Window('Menu Procedimento', layout, modal=True, element_justification='c')
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
            [sg.Text('Descrição do procedimento:'), sg.InputText(key='descricao')],
            [sg.Text('Custo (R$):'), sg.InputText(key='custo')],
            [sg.Text('CPF do profissional responsável:'), sg.InputText(key='cpf_profissional')],
            [sg.Text('Número do atendimento vinculado:'), sg.InputText(key='index')],
            [sg.Button('Registrar'), sg.Button('Cancelar', button_color=('white', 'gray'))]
        ]
        window = sg.Window('Registrar Procedimento', layout, modal=True)
        event, values = window.read()
        
        if event == 'Registrar':
            try:
                descricao = values['descricao'].strip()
                custo = float(values['custo'].strip())
                cpf_profissional = values['cpf_profissional'].strip()
                index = int(values['index'].strip()) - 1
                
                self.__controlador_procedimento.cadastrar(descricao, custo, cpf_profissional, index)
                sg.popup('Procedimento registrado com sucesso!', title='Sucesso')
            except ProcedimentoException as e:
                sg.popup_error(f'Erro: {e}', title='Erro')
            except Exception as e:
                sg.popup_error(f'Erro: {e}', title='Erro')
        window.close()

    def remover(self):
        layout = [
            [sg.Text('Número do procedimento a remover:'), sg.InputText(key='index')],
            [sg.Button('Remover', button_color=('white', 'red')), sg.Button('Cancelar', button_color=('white', 'gray'))]
        ]
        window = sg.Window('Remover Procedimento', layout, modal=True)
        event, values = window.read()
        if event == 'Remover':
            try:
                index = int(values['index'].strip()) - 1
                self.__controlador_procedimento.remover(index)
                sg.popup('Procedimento removido com sucesso!', title='Sucesso')
            except ProcedimentoException as e:
                sg.popup_error(f'Erro: {e}', title='Erro')
            except Exception as e:
                sg.popup_error(f'Erro: {e}', title='Erro')
        window.close()

    def alterar(self):
        layout = [
            [sg.Text('Número do procedimento a alterar:'), sg.InputText(key='index')],
            [sg.Text('Novos dados (deixe em branco para manter):', font=('Helvetica', 10, 'bold'))],
            [sg.Text('Nova descrição:'), sg.InputText(key='descricao')],
            [sg.Text('Novo custo (R$):'), sg.InputText(key='custo')],
            [sg.Text('Novo CPF do profissional responsável:'), sg.InputText(key='cpf_profissional')],
            [sg.Button('Alterar'), sg.Button('Cancelar', button_color=('white', 'gray'))]
        ]
        window = sg.Window('Alterar Procedimento', layout, modal=True)
        event, values = window.read()
        if event == 'Alterar':
            try:
                index = int(values['index'].strip()) - 1
                descricao = values['descricao'].strip() or None
                custo_str = values['custo'].strip()
                custo = float(custo_str) if custo_str else None
                cpf_profissional = values['cpf_profissional'].strip() or None
                
                self.__controlador_procedimento.alterar(index, descricao, custo, cpf_profissional)
                sg.popup('Procedimento alterado com sucesso!', title='Sucesso')
            except ProcedimentoException as e:
                sg.popup_error(f'Erro: {e}', title='Erro')
            except Exception as e:
                sg.popup_error(f'Erro: {e}', title='Erro')
        window.close()

    def listar(self):
        try:
            procedimentos = self.__controlador_procedimento.listar()
            text = "=== PROCEDIMENTOS ===\n\n"
            for i, p in enumerate(procedimentos):
                text += f"{i+1}. {p['descricao']} | Custo: R${p['custo']:.2f} | Profissional: {p['profissional']}\n"
            sg.popup_scrolled(text, title='Listar Procedimentos', size=(60, 15))
        except ProcedimentoException as e:
            sg.popup_error(f'Erro: {e}', title='Erro')