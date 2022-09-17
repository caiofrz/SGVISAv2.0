class Estabelecimento:
    def __init__(self, razao_social, cnpj, telefone, atividade_economica, data_validade_alvara, situacao):
        self.razao_social = razao_social
        self.cnpj = cnpj
        self.telefone = telefone
        self.atividade_economica = atividade_economica
        self.data_validade_alvara = data_validade_alvara
        self.situacao = situacao

    def __str__(self):
        return f'{self.razao_social}\t{self.cnpj}\t{self.telefone}\t{self.atividade_economica}\t' \
               f'{self.data_validade_alvara}\t{self.situacao}'

