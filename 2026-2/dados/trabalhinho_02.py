# Trabalhinho 02 - Lista encadeada simples

class Numero:
    def __init__(self, valor):
        self.valor = valor
        self.proximo = None

class Lista:
    def __init__(self):
        self.primeiro = None
        self.ultimo = None

    # Inserção de elemento
    
    def InserirComoPrimeiro(self, valor):
        novo = Numero(valor)

        novo.proximo = self.primeiro
        self.primeiro = novo

    def InserirComoUltimo(self, valor):
        novo = Numero(valor)
        
        if self.primeiro is not None:
            atual = self.primeiro
            while atual.proximo is not None:
                atual = atual.proximo
            atual.proximo = novo
        else:
            self.primeiro = novo

    # Terminar
    def InserirNaPosicao(self, posicao, valor):
        novo = Numero(valor)
        
        if self.primeiro is not None:
            atual = self.primeiro
            
            while atual.proximo is not posicao:
                atual = atual.proximo
            atual.proximo = novo
        else:
            self.primeiro = novo
    
    # Continuar daqui em diante
    def InserirAntesDe(self, referencia, valor):
            novo = Numero(valor)
                    
            if self.primeiro is not None:
                atual = self.primeiro
                
                while atual.proximo.proximo is not referencia:
                    atual = atual.proximo
                atual.proximo = novo
            else:
                self.primeiro = novo
    
    def InserirDepoisDe(self, referencia, valor):
            novo = Numero(valor)
                                
            if self.primeiro is not None:
                atual = self.primeiro
                
                while atual.proximo.proximo is not valor:
                    atual = atual.proximo
                atual.proximo = novo
            else:
                self.primeiro = novo
    
    
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
