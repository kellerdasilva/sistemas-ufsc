class Noh:
    def __init__(self, dado):
        self.dado = dado
        self.prox = None

class FilaEncadeada:
    def __init__(self):
        self.prim = None
        self.ult = None

    def estah_vazia(self):
        # TODO
        pass

    def entra(self, x):
        novo = Noh(x)
        # TODO: dois casos:
        #   - fila vazia: o novo nó é ao mesmo tempo prim e ult
        #   - fila com elementos: liga o ult atual ao novo e atualiza ult
        pass

    def sai(self):
        # TODO: se estiver vazia, avise
        # senão: guarde o dado de prim, avance prim para o prox
        #        e trate o caso em que a fila ficou vazia (o que ult deve ser?)
        pass
