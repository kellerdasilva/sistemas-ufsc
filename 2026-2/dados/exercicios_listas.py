class Numero:
    def __init__(self, valor):
        self.valor = valor
        self.proximo = None

class Lista:
    def __init__(self):
        self.primeiro = None
        self.ultimo = None

    def InserirComoPrimeiro(self, novo):
        novo.proximo = self.primeiro
        self.primeiro = novo

    def InserirComoUltimo(self, novo):
        if self.primeiro is None:
            self.primeiro = novo
        else:
            atual = self.primeiro
            while atual.proximo is not None:
                atual = atual.proximo
            atual.proximo = novo

    def RemoverPrimeiro(self):
        if self.primeiro is not None:
            self.primeiro = self.primeiro.proximo

    def RemoverUltimo(self):
        if self.primeiro is not None:
            atual = self.primeiro
            
        while atual.proximo is not None:
            atual = atual.proximo

    def Remover(self, valor):
        if self.primeiro is not None:
            atual = self.primeiro
            
        while atual.proximo.valor is not valor:
            atual = atual.proximo
        atual.proximo = atual.proximo.proximo

    def AcessaPrimeiro(self):
        if self.primeiro is not None:
            return self.primeiro.valor
