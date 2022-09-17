class Funcionario:
    def __init__(self, nome, cpf, telefone, funcao):
        self.nome = nome
        self.cpf = cpf
        self.telefone = telefone
        self.funcao = funcao

    def __str__(self):
        #return f'NOME: {self.nome} - CPF: {self.cpf} - TEL: {self.telefone} - FUNÇÃO: {self.funcao}'
        return f'{self.nome}\t{self.cpf}\t{self.telefone}\t{self.funcao}'

    def get_cpf(self):
        return self.cpf


