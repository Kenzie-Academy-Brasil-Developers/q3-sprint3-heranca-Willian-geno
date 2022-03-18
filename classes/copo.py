from classes import Recipiente

class Copo(Recipiente):
    def __init__(self, tamanho: float = 0, conteudo: float = 0, limpo: bool = True):
        super().__init__(tamanho, conteudo, limpo)

    def encher (self, bebida:str = "água"):
        if not self.limpo:
            return "Não se pode encher um copo sujo"
        self.bebida= bebida
        self.conteudo = self.tamanho
        self.limpo= False

    def beber(self, quantidade:float):
        if quantidade < 0:
            return "Quantidade deve ser positiva" 
        if quantidade > self.tamanho:
            return "Não há bebida suficiente no copo"
        self.conteudo = self.conteudo - quantidade

    def lavar (self):
        self.bebida = None
        self.limpo = True
        self.conteudo = 0

    def __str__ (self):
        if self.conteudo == 0:
            return f'Um copo vazio de {self.tamanho}ml'
        else:
            return f'Um copo de {self.tamanho}ml contendo {self.conteudo}ml de {self.bebida}'

    def __repr__ (self):
        if self.conteudo == 0:
            return f'Um copo vazio de {self.tamanho}ml'
        else:
            return f'Um copo de {self.tamanho}ml contendo {self.conteudo}ml de {self.bebida}'