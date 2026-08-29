# ======
# PILHA
# ======

class ElementoPilha:

    def __init__(self, valor):
        self.valor = valor
        self.ant = None  # aponta pro elemento que estava embaixo dele

class Pilha:

    def __init__(self):
        self.topo = None  # aponta pro elemento do topo da pilha

    def vazia(self):
        return self.topo is None

    def push(self, valor):
        novo = ElementoPilha(valor)
        novo.ant = self.topo   # o novo elemento aponta pra quem era o topo
        self.topo = novo       # o topo passa a ser o novo elemento
        print(f"[PILHA] PUSH({valor})")

    def pop(self):
        if self.vazia():
            print("[PILHA] POP: pilha vazia!")
            return None

        removido = self.topo
        self.topo = removido.ant  # o topo passa a ser o elemento anterior
        removido.ant = None       # desfaz o apontamento do removido
        print(f"[PILHA] POP() -> {removido.valor}")
        return removido.valor

    def imprime(self):
        print("PILHA (topo -> base): ", end="")
        atual = self.topo
        if atual is None:
            print("(vazia)")
            return
        valores = []
        while atual is not None:
            valores.append(str(atual.valor))
            atual = atual.ant
        print(" -> ".join(valores))

# =====
# FILA
# =====

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
            # o antigo último elemento passa a apontar para o novo
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

# ================
# CLASSE DE TESTE
# ================

class Teste:

    def __init__(self):
        self.pilha = Pilha()
        self.fila = Fila()

    def executar(self):
        print("=" * 15)
        print("TESTE - PILHA")
        print("=" * 15)

        self.pilha.push(7)
        self.pilha.push(3)
        self.pilha.push(9)
        self.pilha.imprime()

        self.pilha.push(42)
        self.pilha.imprime()

        self.pilha.pop()
        self.pilha.pop()
        self.pilha.imprime()

        print()
        print("=" * 15)
        print("TESTE - FILA")
        print("=" * 15)

        self.fila.entra(1)
        self.fila.entra(4)
        self.fila.entra(2)
        self.fila.imprime()

        self.fila.entra(12)
        self.fila.imprime()

        self.fila.sai()
        self.fila.sai()
        self.fila.imprime()

if __name__ == "__main__":
    teste = Teste()
    teste.executar()
