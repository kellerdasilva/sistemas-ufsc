class Numero:
    def __init__(self, valor):
        self.valor = valor
        self.proximo = None

class Lista:
    def __init__(self):
        self.primeiro = None
        self.ultimo = None

    # Inserção de elemento
    
    def InserirComoPrimeiro(self, novo):
        novo_numero = Numero(novo)

        novo_numero.proximo = self.primeiro
        self.primeiro = novo_numero

    def InserirComoUltimo(self, novo):
        novo_numero = Numero(novo)
        
        if self.primeiro is not None:
            atual = self.primeiro
            while atual.proximo is not None:
                atual = atual.proximo
            atual.proximo = novo_numero
        else:
            self.primeiro = novo_numero

    # Terminar
    def InserirNaPosicao(self, posicao, novo):
        novo_numero = Numero(novo)
        
        if self.primeiro is not None:
            atual = self.primeiro
            
            while atual.proximo is not posicao:
                atual = atual.proximo
            atual.proximo = novo_numero
        else:
            self.primeiro = novo_numero
    
    # Continuar daqui em diante
    def InserirAntesDe(self, valor, novo):
            novo_numero = Numero(novo)
                    
            if self.primeiro is not None:
                atual = self.primeiro
                
                while atual.proximo.proximo is not valor:
                    atual = atual.proximo
                atual.proximo = novo_numero
            else:
                self.primeiro = novo_numero
    
    def InserirDepoisDe(referencia, novo):
            novo_numero = Numero(novo)
                                
            if self.primeiro is not None:
                atual = self.primeiro
                
                while atual.proximo.proximo is not valor:
                    atual = atual.proximo
                atual.proximo = novo_numero
            else:
                self.primeiro = novo_numero
    
    
    # Remoção de elemento
    
    def RemoverPrimeiro(self):
        if self.primeiro is not None:
            self.primeiro = self.primeiro.proximo

    def RemoverUltimo(self):
        if self.primeiro is not None:
            atual = self.primeiro
            
        while atual.proximo is not None:
            atual = atual.proximo

    def RemoverDaPosicao(self, posicao):
        pass
    
    def Remover(self, valor):
        if self.primeiro is not None:
            atual = self.primeiro

        while atual.proximo.valor is not valor:
            atual = atual.proximo
        atual.proximo = atual.proximo.proximo

    # Consulta/acesso
    
    def AcessaPrimeiro(self):
        if self.primeiro is not None:
            return self.primeiro.valor

    def AcessaUltimo(self):
        pass
    
    def AcessaDaPosicao(posicao):
        pass

    def Busca(referencia):
        pass
