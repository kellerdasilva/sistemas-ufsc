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
