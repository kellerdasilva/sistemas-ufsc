# Exercício 02

# Criar classe Livro
class Livro:
    def __init__(self, codigo, titulo, resumo, autor, protagonista, genero, faixa_etaria):
        self.codigo = codigo
        self.titulo = titulo
        self.resumo = resumo
        self.autor = autor
        self.protagonista = protagonista
        self.genero = genero
        self.faixa_etaria = faixa_etaria
    
    # Código
    @property
    def codigo(self):
        return self._codigo
    
    @codigo.setter
    def codigo(self, valor):
        self._codigo = valor
    
    # Título
    @property
    def titulo(self):
        return self._titulo
    
    @titulo.setter
    def titulo(self, valor):
        self._titulo = valor
    
    # Resumo
    @property
    def resumo(self):
        return self._resumo
    
    @resumo.setter
    def resumo(self, valor):
        self._resumo = valor
    
    # Autor
    @property
    def autor(self):
        return self._autor
    
    @autor.setter
    def autor(self, valor):
        self._autor = valor
        
    # Protagonista
    @property
    def protagonista(self):
        return self._protagonista
    
    @protagonista.setter
    def protagonista(self, valor):
        self._protagonista = valor
        
    # Gênero
    @property
    def genero(self):
        return self._genero
    
    @genero.setter
    def genero(self, valor):
        self._genero = valor
        
    # Faixa etária
    @property
    def faixa_etaria(self):
        return self._faixa_etaria
    
    @faixa_etaria.setter
    def faixa_etaria(self, valor):
        self._faixa_etaria = valor