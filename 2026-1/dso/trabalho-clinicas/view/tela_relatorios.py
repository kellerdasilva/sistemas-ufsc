import FreeSimpleGUI as sg
from Exceptions.atendimentoException import AtendimentoException
from Exceptions.procedimentoException import ProcedimentoException

class TelaRelatorios:
    def __init__(self, controlador_atendimento, controlador_procedimento):
        self.__controlador_atendimento = controlador_atendimento
        self.__controlador_procedimento = controlador_procedimento

    def mostrar_menu(self):
        layout = [
            [sg.Text('=== MENU RELATÓRIOS ===', font=('Helvetica', 14, 'bold'))],
            [sg.Button('1. Clínicas com maior número de atendimentos', key='1', size=(40, 1))],
            [sg.Button('2. Atendimentos mais caros e mais baratos', key='2', size=(40, 1))],
            [sg.Button('3. Procedimentos mais realizados', key='3', size=(40, 1))],
            [sg.Button('4. Procedimentos mais caros e mais baratos', key='4', size=(40, 1))],
            [sg.Button('Voltar', key='0', size=(10, 1), button_color=('white', 'gray'))]
        ]
        window = sg.Window('Menu Relatórios', layout, modal=True, element_justification='c')
        while True:
            event, values = window.read()
            if event == sg.WIN_CLOSED or event == '0':
                break
            elif event == '1':
                self.clinicas_mais_atendimentos()
            elif event == '2':
                self.atendimentos_mais_caros_baratos()
            elif event == '3':
                self.procedimentos_mais_populares()
            elif event == '4':
                self.procedimentos_mais_caros_baratos()
        window.close()

    def clinicas_mais_atendimentos(self):
        try:
            ranking = self.__controlador_atendimento.relatorio_clinicas_mais_atendimentos()
            text = "=== CLÍNICAS COM MAIS ATENDIMENTOS ===\n\n"
            for i, (clinica, qtd) in enumerate(ranking):
                text += f"{i+1}. {clinica} | Atendimentos: {qtd}\n"
            sg.popup_scrolled(text, title='Relatório', size=(60, 15))
        except AtendimentoException as e:
            sg.popup_error(f'Erro: {e}', title='Erro')

    def atendimentos_mais_caros_baratos(self):
        try:
            resultado = self.__controlador_atendimento.relatorio_atendimentos_mais_caros_baratos()
            text = "=== ATENDIMENTOS MAIS CAROS ===\n"
            for a in resultado["mais_caros"]:
                text += f"  {a['data']} | {a['paciente']} | R${a['valor_total']:.2f}\n"
            
            text += "\n=== ATENDIMENTOS MAIS BARATOS ===\n"
            for a in resultado["mais_baratos"]:
                text += f"  {a['data']} | {a['paciente']} | R${a['valor_total']:.2f}\n"
            sg.popup_scrolled(text, title='Relatório', size=(60, 15))
        except AtendimentoException as e:
            sg.popup_error(f'Erro: {e}', title='Erro')

    def procedimentos_mais_populares(self):
        try:
            ranking = self.__controlador_procedimento.relatorio_mais_populares()
            text = "=== PROCEDIMENTOS MAIS REALIZADOS ===\n\n"
            for i, (descricao, qtd) in enumerate(ranking):
                text += f"{i+1}. {descricao} | Realizações: {qtd}\n"
            sg.popup_scrolled(text, title='Relatório', size=(60, 15))
        except ProcedimentoException as e:
            sg.popup_error(f'Erro: {e}', title='Erro')

    def procedimentos_mais_caros_baratos(self):
        try:
            resultado = self.__controlador_procedimento.relatorio_mais_caros_baratos()
            text = "=== PROCEDIMENTOS MAIS CAROS ===\n"
            for p in resultado["mais_caros"]:
                text += f"  {p['descricao']} | R${p['custo']:.2f}\n"
            
            text += "\n=== PROCEDIMENTOS MAIS BARATOS ===\n"
            for p in resultado["mais_baratos"]:
                text += f"  {p['descricao']} | R${p['custo']:.2f}\n"
            sg.popup_scrolled(text, title='Relatório', size=(60, 15))
        except ProcedimentoException as e:
            sg.popup_error(f'Erro: {e}', title='Erro')
