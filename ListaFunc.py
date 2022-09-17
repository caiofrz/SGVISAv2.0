from no import No


class ListaFunc:
    def __init__(self):
        self.raiz = None

    def menor(self):
        return self.menor_aux(self.raiz)

    def menor_aux(self, no):
        if no.esquerda is None:
            return no

        return self.maior_aux(no.esquerda)

    def maior(self):
        return self.maior_aux(self.raiz)

    def maior_aux(self, no):
        if no.direita is None:
            return no

        return self.maior_aux(no.direita)

    def inserir(self, dado, chave):
        self.raiz = self.inserir_aux(dado, chave, self.raiz)

    def inserir_aux(self, dado, chave, no):
        if no == None:
            return No(chave, dado)

        elif chave < no.chave:
            no.esquerda = self.inserir_aux(dado, chave, no.esquerda)

        else:
            no.direita = self.inserir_aux(dado, chave, no.direita)

        return no

    def printERD(self):
        self.print_aux(self.raiz)

    def print_aux(self, no):
        if no != None:
            self.print_aux(no.esquerda)
            print(no.dado)
            self.print_aux(no.direita)

    def excluir(self, valor):
        self.raiz = self.excluir_aux(self.raiz, valor)

    def excluir_aux(self, no, valor):

        if no is None:
            return None

        elif valor > no.chave:
            no.direita = self.excluir_aux(no.direita, valor)

        elif valor < no.chave:
            no.esquerda = self.excluir_aux(no.esquerda, valor)
        else:
            if no.esquerda is None:
                return no.direita

            elif no.direita is None:
                return no.esquerda

            else:
                menor = self.menor_aux(no.direita)
                no.dado = menor.dado
                no.direita = self.excluir_aux(no.direita, menor.dado)

        return no

    def arq(self):
        f = open('VisaFuncionario.txt', 'w', encoding="UTF-8")
        self.arq_aux(self.raiz, f)
        f.close()

    def arq_aux(self, no, f):
        if no != None:
            self.arq_aux(no.esquerda, f)
            f.write(str(no.dado))
            f.write('\n')
            self.arq_aux(no.direita, f)
