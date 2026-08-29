class ElementoFila:

    def __init__(self, valor):
        self.valor = valor
        self.prox = None  # aponta pro próximo elemento da fila

class Fila:

    def __init__(self):
        self.inicio = None  # aponta pro primeiro elemento (quem sai)
        self.fim = None     # aponta pro último elemento (onde entra)

    def vazia(self):
        return self.inicio is None

    def entra(self, valor):
        novo = ElementoFila(valor)

        if self.vazia():
            # fila estava vazia: novo elemento é início e fim ao mesmo tempo
            self.inicio = novo
            self.fim = novo
        else:
            # o antigo último elemento passa a apontar pro novo
            self.fim.prox = novo
            self.fim = novo

        print(f"[FILA] ENTRA({valor})")

    def sai(self):
        if self.vazia():
            print("[FILA] SAI: fila vazia!")
            return None

        removido = self.inicio
        self.inicio = removido.prox  # início passa a ser o próximo elemento

        if self.inicio is None:
            # a fila ficou vazia, fim também deve ser atualizado
            self.fim = None

        removido.prox = None
        print(f"[FILA] SAI() -> {removido.valor}")
        return removido.valor

    def imprime(self):
        print("FILA (inicio -> fim): ", end="")
        atual = self.inicio
        if atual is None:
            print("(vazia)")
            return
        valores = []
        while atual is not None:
            valores.append(str(atual.valor))
            atual = atual.prox
        print(" -> ".join(valores))
