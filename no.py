class No:
    def __init__(self, chave, dado):
        self.chave = chave
        self.dado = dado
        self.esquerda = None
        self.direita = None

    def __str__(self):
        return self.dado