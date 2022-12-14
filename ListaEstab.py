from no import No


class ListaEstab:
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

    def situacao(self, cnpj):
        with open('VisaEstabelecimento.txt', 'r', encoding="UTF-8") as arquivo:
            for v in arquivo:
                dado = v.replace('\n', '').split('\t')

                if cnpj == dado[1]:
                    if dado[5] == '1':
                        print(f'{dado[0]}|Situa????o do Alvar?? Sanit??rio\033[33m\n '
                              f'Aguarda cumprimento de ressalvas para Alvar?? Inicial\033[m')
                        return
                    elif dado[5] == '2':
                        print(f'{dado[0]}| Situa????o do Alvar?? Sanit??rio\033[31m\nInterdi????o cautelar\033[m')
                        return
                    elif dado[5] == '3':
                        print(f'{dado[0]}| Situa????o do Alvar?? Sanit??rio\033[31m\n'
                              f'N??o protocolou situa????o de renova????o de Alvar??\033[m')
                        return
                    elif dado[5] == '4':
                        print(f'{dado[0]}| Situa????o do Alvar?? Sanit??rio\033[32m\n'
                              f'Alvar?? vigente e dentro do prazo para solicita????o de renova????o\033[m')
                        return
                    elif dado[5] == '5':
                        print(f'{dado[0]}| Situa????o do Alvar?? Sanit??rio\033[31m\n'
                              f'Alvar?? vencido e estabelecimento n??o cumpriu ressalvas apontadas no Relat??rio de '
                              f'Inspe????o\033[m')
                        return
                    elif dado[5] == '6':
                        print(f'{dado[0]}| Situa????o do Alvar?? Sanit??rio\033[33m\n'
                              f'Atividade n??o sujeita a concess??o de Alvar?? Sanit??rio\033[m')
                        return
                    elif dado[5] == '7':
                        print(f'{dado[0]}| Situa????o do Alvar?? Sanit??rio\033[32m\n'
                              f'Alvar?? vencido, protocolou solicita????o de renova????o e aguarda inspe????o\033[m')
                        return

    def arq_estab(self):
        f = open('VisaEstabelecimento.txt', 'w', encoding="UTF-8")
        self.arqEstab_aux(self.raiz, f)
        f.close()

    def arqEstab_aux(self, no, f):
        if no != None:
            self.arqEstab_aux(no.esquerda, f)
            f.write(str(no.dado))
            f.write('\n')
            self.arqEstab_aux(no.direita, f)

