import FreeSimpleGUI as sg
from Exceptions.pagamentoException import PagamentoException

class TelaPagamento:
    def __init__(self, controlador_pagamento):
        self.__controlador_pagamento = controlador_pagamento

    def mostrar_menu(self):
        layout = [
            [sg.Text('=== MENU PAGAMENTO ===', font=('Helvetica', 14, 'bold'))],
            [sg.Button('Registrar pagamento', key='1', size=(25, 1))],
            [sg.Button('Remover pagamento', key='2', size=(25, 1))],
            [sg.Button('Alterar pagamento', key='3', size=(25, 1))],
            [sg.Button('Listar pagamentos', key='4', size=(25, 1))],
            [sg.Button('Voltar', key='0', size=(10, 1), button_color=('white', 'gray'))]
        ]
        window = sg.Window('Menu Pagamento', layout, modal=True, element_justification='c')
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
            [sg.Text('Número do atendimento a pagar:'), sg.InputText(key='index')],
            [sg.Text('Data do pagamento (AAAA-MM-DD):'), sg.InputText(key='data')],
            [sg.Text('Valor pago (R$):'), sg.InputText(key='valor_pago')],
            [sg.Text('Tipo de pagamento:'), sg.Combo(['dinheiro', 'pix', 'cartao'], key='tipo', readonly=True)],
            [sg.Text('CPF do pagador (se PIX):'), sg.InputText(key='cpf_pagador')],
            [sg.Text('Número do cartão (se Cartão):'), sg.InputText(key='numero_cartao')],
            [sg.Text('Bandeira do cartão (se Cartão):'), sg.InputText(key='bandeira_cartao')],
            [sg.Button('Registrar'), sg.Button('Cancelar', button_color=('white', 'gray'))]
        ]
        window = sg.Window('Registrar Pagamento', layout, modal=True)
        event, values = window.read()
        
        if event == 'Registrar':
            try:
                index = int(values['index'].strip()) - 1
                data = values['data'].strip()
                valor_pago = float(values['valor_pago'].strip())
                tipo = values['tipo']
                
                cpf_pagador = values['cpf_pagador'].strip() or None
                numero_cartao = values['numero_cartao'].strip() or None
                bandeira_cartao = values['bandeira_cartao'].strip() or None

                self.__controlador_pagamento.cadastrar(
                    tipo, data, valor_pago, index,
                    cpf_pagador, numero_cartao, bandeira_cartao
                )
                sg.popup('Pagamento registrado com sucesso!', title='Sucesso')
            except PagamentoException as e:
                sg.popup_error(f'Erro: {e}', title='Erro')
            except ValueError:
                sg.popup_error('Erro: Tipo de dado inválido fornecido.', title='Erro')
        window.close()

    def remover(self):
        layout = [
            [sg.Text('Número do pagamento a remover:'), sg.InputText(key='index')],
            [sg.Button('Remover', button_color=('white', 'red')), sg.Button('Cancelar', button_color=('white', 'gray'))]
        ]
        window = sg.Window('Remover Pagamento', layout, modal=True)
        event, values = window.read()
        if event == 'Remover':
            try:
                index = int(values['index'].strip()) - 1
                self.__controlador_pagamento.remover(index)
                sg.popup('Pagamento removido com sucesso!', title='Sucesso')
            except PagamentoException as e:
                sg.popup_error(f'Erro: {e}', title='Erro')
            except ValueError:
                sg.popup_error('Erro: Tipo de dado inválido fornecido.', title='Erro')
        window.close()

    def alterar(self):
        layout = [
            [sg.Text('Número do pagamento a alterar:'), sg.InputText(key='index')],
            [sg.Text('Novos dados (deixe em branco para manter):', font=('Helvetica', 10, 'bold'))],
            [sg.Text('Nova data (AAAA-MM-DD):'), sg.InputText(key='data')],
            [sg.Text('Novo valor pago (R$):'), sg.InputText(key='valor_pago')],
            [sg.Button('Alterar'), sg.Button('Cancelar', button_color=('white', 'gray'))]
        ]
        window = sg.Window('Alterar Pagamento', layout, modal=True)
        event, values = window.read()
        if event == 'Alterar':
            try:
                index = int(values['index'].strip()) - 1
                data = values['data'].strip() or None
                valor_str = values['valor_pago'].strip()
                valor_pago = float(valor_str) if valor_str else None
                
                self.__controlador_pagamento.alterar(index, data, valor_pago)
                sg.popup('Pagamento alterado com sucesso!', title='Sucesso')
            except PagamentoException as e:
                sg.popup_error(f'Erro: {e}', title='Erro')
            except ValueError:
                sg.popup_error('Erro: Tipo de dado inválido fornecido.', title='Erro')
        window.close()

    def listar(self):
        try:
            pagamentos = self.__controlador_pagamento.listar()
            text = "=== PAGAMENTOS ===\n\n"
            for i, p in enumerate(pagamentos):
                text += f"{i+1}. Data: {p['data']} | Valor pago: R${p['valor_pago']:.2f} | Tipo: {p['tipo']}\n"
            sg.popup_scrolled(text, title='Listar Pagamentos', size=(60, 15))
        except PagamentoException as e:
            sg.popup_error(f'Erro: {e}', title='Erro')