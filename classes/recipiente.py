class Recipiente:

    def __init__(self, tamanho:float = 0, conteudo: float = 0, limpo:bool = True):
        self.tamanho = tamanho if tamanho >= 0 else 0
        self.conteudo = conteudo if conteudo >= 0 else 0
        self.limpo = limpo


    def esvaziar(self):
        self.conteudo = 0
    
    def esta_vazio(self):
        if self.conteudo == 0:
            return True
        else:
            return False
    
    def lavar(self):
        self.conteudo = 0
        self.limpo = True

    def  esta_limpo(self):
        return self.limpo

    def estado(self):
        if self.limpo:
            return "limpo"
        else:
            return "sujo"

    def sujar(self):
        self.limpo = False
            

    def __repr__(self):
        if self.limpo:
            return f'Um recipiente limpo não especificado'
        else:
            return f'Um recipiente sujo não especificado'


    def __str__(self):
        if self.limpo:
            return f'Um recipiente limpo não especificado'
        else:
            return f'Um recipiente sujo não especificado'