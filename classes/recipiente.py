class Recipiente:

    def __init__(self, tamanho:float = 0, conteudo: float = 0, limpo:bool = True):
        self.tamanho = tamanho if tamanho >= 0 else 0
        self.conteudo = conteudo if conteudo >= 0 else 0
        self.linpo = limpo


    def esvaziar(self):
        self.conteudo = 0
    
    def esta_vazio(self):
        if self.conteudo == 0:
            return True
        else:
            return False
    
    def lavar(self):
        self.conteudo = 0
        self.linpo = True

    def  esta_limpo(self):
        return self.linpo

    def estado(self):
        if self.linpo:
            return "limpo"
        else:
            return "sujo"

    def sujar(self):
        self.linpo = False
            

    def __repr__(self):
        if self.linpo:
            return f'Um recipiente limpo não especificado'
        else:
            return f'Um recipiente sujo não especificado'


    def __str__(self):
        if self.linpo:
            return f'Um recipiente limpo não especificado'
        else:
            return f'Um recipiente sujo não especificado'