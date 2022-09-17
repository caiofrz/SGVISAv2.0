class Visita:
    def __init__(self, razão_sozial, cnpj, data_visita):
        self.razão_sozial = razão_sozial
        self.cnpj = cnpj
        self.data_visita = data_visita

    def __str__(self):
        return f'{self.razão_sozial}\t{self.cnpj}\t{self.data_visita}'

