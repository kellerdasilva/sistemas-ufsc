from pilha import Pilha
from fila import Fila

class Teste:

    def __init__(self):
        self.pilha = Pilha()
        self.fila = Fila()

    def executar(self):
        print("=" * 15)
        print("TESTE - PILHA")
        print("=" * 15)
        print()

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
        print()

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
