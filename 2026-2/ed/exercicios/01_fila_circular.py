class FilaCircular:
    def __init__(self, tamanho):
        self.dados = [None] * tamanho
        self.tamanho = tamanho
        self.inicio = 0
        self.fim = 0
        self.qtd = 0
    
    def estah_vazia(self):
        return self.qtd == 0
    
    def estah_cheia(self):
        return self.qtd == self.tamanho
    
    def entra(self, x):
        if self.estah_cheia():
            print("A fila já está cheia.")
        else:
            self.dados[self.fim] = x
            self.fim = (self.fim + 1) % self.tamanho
            self.qtd += 1
            
    def sai(self):
        if self.estah_vazia():
            print ("A fila já está vazia.")
        else:
            x = self.dados[self.inicio]
            self.dados[self.inicio] = None
            self.inicio = (self.inicio + 1) % self.tamanho
            self.qtd -= 1
            return x

# Testando

fila = FilaCircular(5)

def estado():
    print(f"{fila.dados}\nInício = {fila.inicio}\nFim = {fila.fim}\nQuantidade = {fila.qtd}")

fila.entra("A")
fila.entra("B")
fila.entra("C")
fila.sai()
fila.sai()
fila.entra("D")
fila.entra("E")
fila.entra("F")
estado()

fila.entra("G")
estado()

fila.entra("H")
estado()
